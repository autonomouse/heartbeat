$(document).ready(function() {
    // timer function
    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        var refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10)
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            var output = minutes + " : " + seconds;
            display.text(output);
            $("title").html(output + " - Heartbeat");

            if (--timer < 0) {
                display.text("Time's Up!");
                clearInterval(refresh);  // exit refresh loop
                var music = $("#over_music")[0];
                music.play();
                alert("Time's Up!");
            }
        }, 1000);

    }

    var txt = '300';

    var unicorn = parseInt(txt);

    // start timer
    jQuery(function ($) {
        var display = $('#time');
        startTimer(unicorn, display);
    });

    // show help information
    $('#help-info').hide();
    $('#help-btn').hover( function() { $('#help-info').toggle(); } );
})