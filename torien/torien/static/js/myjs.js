$(".itemflex").click(function () {
    $(".content").show();
});
$(window).on("scroll", function () {
    sT = $(window).scrollTop();
    wH = $(window).height();
    x = sT * 100 / wH;
    if (x > 100) {
        $('.embed-responsive-item, .video-overlay').css('display', 'none');
    } else {
        // $('.video-overlay').css({'opacity': 1 - ((x - 20) / 20)});
        $('.video-overlay').css({ 'opacity': (x / 100) });
        $('.embed-responsive-item, .video-overlay').css('display', 'block');
    }
});