function myFunction1() {
  var x = document.getElementById("myDIV");
  if (x.innerHTML === "Click to know the winner of the Lucky Draw!") {
    x.innerHTML = "{{ competition.competitionWinner.participant }}";
  } else {
    x.innerHTML = "User444s";
  }
}

