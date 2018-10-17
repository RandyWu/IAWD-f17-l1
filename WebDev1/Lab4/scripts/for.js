var minimum = Number(prompt("Input a minimum value: ",""));
var maximum = Number(prompt("Input a maximum value: ",""));
var increase = Number(prompt("Input a increase value: ",""));

function setForLoopValues(starting, ending, increment){
  for (var i = starting; i <= ending; i += increment){
      document.writeln('</br>' + i);
  }
}

setForLoopValues(minimum, maximum, increase);
