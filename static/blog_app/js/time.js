var timeDisplay = document.getElementById("time_id");


function refreshTime() {
  var dateString = new Date().toLocaleString("en-in", {timeZone: "UTC"});
//  var dateString = new Date()
  var formattedString = dateString.replace(", ", " - ");
  timeDisplay.innerHTML = formattedString;
}

setInterval(refreshTime, 1000);