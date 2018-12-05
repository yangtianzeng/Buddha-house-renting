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

                console.log(span.children(".glyphicon-heart"))
                span.children(".glyphicon-heart").attr("style","color: red")
                var num = span.children(".lnum").html()
                num = parseInt(num)+1
                span.children(".lnum").html(num)


            }else if (data["status"] == "0") {

                console.log(span.children(".glyphicon-heart"))
                span.children(".glyphicon-heart").attr("style","color: black")
                var num = span.children(".lnum").html()
                num = parseInt(num)-1
                span.children(".lnum").html(num)

            }
        })
    })

    // $(".a").click(function () {
    //     var li = $(this).parent().next()
    //     li.removeClass("active")
    //     $(this).parent().addClass("active")
    // })
    // $(".b").click(function () {
    //     var li = $(this).parent().prev()
    //     li.removeClass("active")
    //     $(this).parent().addClass("active")
    //
    // })
})