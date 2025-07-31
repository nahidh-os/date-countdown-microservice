# Date Countdown Microservice

This microservice reads a future date from `input.txt` and writes the number of days remaining until that date into `output.txt`.

## 📦 How It Works

1. The main program (or user) writes a future date to `input.txt` in the format `YYYY-MM-DD`.
2. The microservice (`countdown-service.py`) reads the date, calculates how many days remain from today, and writes the result to `output.txt`.

**Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call. Do not advise your teammate to use your test program or require them to, your teammate must write all of their own code.
**

Create a test script that launches countdown_calculator.html (the frontend portion of my microservice), the script will enter a future date into the date field and select an option (days, weeks, months, combo) from the dropdown menu, then click the Submit button. This will trigger the backend portion of my microservice, which receives the future date as a JSON object and writes it to input.txt, along with the format (days, weeks, etc.). It then converts the date in input.txt into that particular format (also contained in input.txt) and then performs the necessary calculations to determine how many days/weeks/months/combo the output should be (e.g. '160 days', '22.86 weeks', etc.) before writing that to output.txt. 

Example call (I used Selenium WebDriver - code written in Python): 

driver.get("path to the file/countdown_calculator.html")

target_date = driver.find_element(By.ID, "targetDate")

target_date.send_keys("01/05/2026")

display_format = driver.find_element(By.ID, "displayFormat")

display_format.send_keys("days")

submit_btn = driver.find_element(By.ID, "submit")

submit_btn.click()

**Clear instructions for how to programmatically RECEIVE data from the microservice you implemented. Include an example call.**

The microservice will do its thing and print the output to output.txt in whichever directory you are calling the microservice from. If no such output.txt file exists, not a problem because a new file with that name will be auto-created and then whatever the output is (e.g. '160 days') will get written to the file. To receive the data you can simply launch the output.txt file using whichever tool you want to (in my case, Selenium WebDriver). 

driver.get("path to the file/output.txt")

<img width="475" height="286" alt="image" src="https://github.com/user-attachments/assets/7d5d8e8f-8f5b-41f5-86db-3645e5931c63" />
