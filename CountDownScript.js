function sendData() {
  const date = document.getElementById("targetDate").value;
  const format = document.getElementById("displayFormat").value;

  if (!date || !format) {
    alert("Please enter both a date and a display format.");
    return;
  }

  fetch("http://127.0.0.1:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      target_date: date,
      display_format: format
    })
  })
  .then(response => response.text())
  .then(data => {
    console.log("Response:", data);
  })
  .catch(error => {
    console.error("Error:", error);
  });

  const dateInput = document.getElementById('targetDate');
  const dateString = dateInput.value;
  var dateObject = new Date(dateString);
  dateObject.setDate(dateObject.getDate() + 1);
  const formattedDate = dateObject.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  alert('The selected date is: ' + formattedDate);

}
