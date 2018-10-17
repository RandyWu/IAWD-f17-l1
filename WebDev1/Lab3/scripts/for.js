var minimum = Number(prompt("Input a minimum value: ",""));
var maximum = Number(prompt("Input a maximum value: ",""));
var increase = Number(prompt("Input a increase value: ",""));

for (var index = minimum; index <= maximum; index += increase){
    document.writeln('</br>' + index);
}
