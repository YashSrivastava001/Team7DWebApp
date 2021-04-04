const realFileBtn = document.getElementById("submission-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");

customBtn.addEventListener("click", function() {
  realFileBtn.click();
});

realFileBtn.addEventListener("change", function() {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
  }
});

function allowVote () {
  // Disable the button
  document.getElementById("voteButton").disabled = true;

  // Do your processing here
  alert("Vote Added!");
}

$(document).ready(function() {
  $('#vote_btn').click(function() {
  var subsubmissionIdVar;
  subsubmissionIdVar = $(this).attr('data-categoryid');
  $.get('/designmytee/vote_submission/',
  {'submission_id': subsubmissionIdVar},
  function(data) {
  $('#vote_count').html(data);
  $('#vote_btn').hide();
  })
  });
  });
