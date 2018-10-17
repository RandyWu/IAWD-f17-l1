var secret = 1;
var guess = prompt("Input a number between 1-10 to try and guess my secret number: ", "");
var congrats = "Congratulations! You are able to guess a random number!"
var failure = "Try again my guy, we are stuck here forever until you get it right: "

do {
    if (guess == secret) {
      document.writeln(congrats,"");
      break;
    }
    else {
      guess = prompt(failure, "");
    }
} while (guess != secret)

document.writeln(congrats);

for(var lol = 0; lol < 100; lol++) {
    document.writeln("<br/>YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY!!!")
}
