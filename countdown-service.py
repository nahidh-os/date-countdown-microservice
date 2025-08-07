from flask import Flask, request, jsonify
import re
from datetime import datetime, date
from flask_cors import CORS

# Create an instance of the Flask application
app = Flask(__name__)
CORS(app)

@app.route('/process', methods=['POST'])
def process_input_and_generate_output():
    data = request.get_json()

    if not data:
        return "No JSON data received", 400

    target_date = data.get("target_date")
    display_format = data.get("display_format")

    if not target_date or not display_format:
        return "Missing target_date or display_format", 400

    try:
        # Write input
        with open("input.txt", "w") as f:
            f.write(f"{target_date}\nformat={display_format}")

        # Read & process
        date_regex = r"\d{4}-\d{2}-\d{2}"
        format_string_only = "%Y-%m-%d"

        with open("input.txt", "r") as file:
            content = file.read()

        result = []
        for line in content.strip().splitlines():
            if line.startswith("format="):
                result.append(line[7:].strip())

        match = re.search(date_regex, content)
        if match:
            target_date_as_date = datetime.strptime(match.group(), format_string_only).date()
            days_remaining = (target_date_as_date - date.today()).days

            if result[0] == "days":
                time_remaining = f"{days_remaining} days"
            elif result[0] == "weeks":
                time_remaining = f"{round(days_remaining / 7, 2)} weeks"
            elif result[0] == "months":
                time_remaining = f"{round(days_remaining / 30, 2)} months"
            elif result[0] == "combo":
                t_months = days_remaining // 30
                t_weeks = (days_remaining % 30) // 7
                t_days = (days_remaining % 30) % 7
                time_remaining = f"{t_months} months, {t_weeks} weeks, {t_days} days"
            else:
                time_remaining = "Invalid format"
        else:
            time_remaining = "Invalid date"

        # Write output
        with open('output.txt', 'w') as f:
            f.write(time_remaining + "\n")

        return f"Result: {time_remaining}", 200

    except Exception as e:
        return f"Error: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
