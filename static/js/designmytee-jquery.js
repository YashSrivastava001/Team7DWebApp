


$(document).ready(function () {
    $('.voteButton').click(function () {
        var subsubmissionIdVar;
        subsubmissionIdVar = $(this).attr('data-submissionid');

        $.get('/designmytee/vote_submission/',
            { 'submission_id': subsubmissionIdVar },
            function (data) {
                $('.vote_count+subsubmissionIdVar').html(data);
                if (!alert('Are you sure?')) { window.location.reload(); }
            })
    });
});


$('.luckyWin').click(function () {
    var LuckyDrawWinner = $(this).attr('data-luckyWinner');
    Str = $(this).html();
    Str = LuckyDrawWinner;
    $(this).html(Str);
});






