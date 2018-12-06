$(function () {
    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        spaceBetween: 30,
        effect: 'fade',
        autoplay: 1000,
        loop: true
    });

    $(".movie-like").click(function () {
        var span = $(this)
        var postid = $(this).attr("postid")
        console.log(postid)

        $.getJSON("/App/add/", {"postid": postid}, function (data) {
            console.log(data["status"])
            if (data["status"] == "777") {

                window.open("/App/login/", target = "_self")
            } else if (data["status"] == "200") {

                pass

            }else if (data["status"] == "0") {

                console.log(span.children(".glyphicon-heart"))

                span.parent().parent().remove()

            }
        })
    })
})