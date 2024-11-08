let guess = prompt("Light or Dark Theme - write 'L' for light or 'D' for dark");
if (guess == "D") {
  alert("You have chosen the dark theme")
  document.body.style.backgroundColor = "black";
  document.body.style.color = "lightcoral";
}
else if (guess == "L") {
  alert("You have chosen the light theme")
}
else {
  alert("Invalid input! Theme set to default: light.")
}
