var index = 0;
var choice = prompt("Enter a number between 0-100", "");

function getNumber(choice) {
  while (index < choice) {
      document.writeln("The value of index is: " + index + "</br>");
      index += 10;
  }
}

getNumber(choice);
