$(function () {

    $.getJSON("/App/load_city/", function (data) {
        var citys_list = data.citys_list
        for (i = 0; i < citys_list.length; i++) {
            var $li = $('<li><a href="#" class="choose_city" onclick="choose_c(this)">' + citys_list[i] + '</a></li>')
            $li.appendTo($('.city'))
        }
    })

    $.getJSON("/App/load_user/", function (data) {
        if (data.is_login) {
            var $li = $('<li>\n' +
                '                            <a href="#"><span>欢迎，' + data.username + '。</span></a>\n' +
                '                        </li>\n' +
                '\n' +
                '                        <li>\n' +
                '                            <a href="#"><span>我的收藏</span></a>\n' +
                '                        </li>\n' +
                '\n' +
                '                        <li>\n' +
                '                            <a href="#"><span>修改信息</span></a>\n' +
                '                        </li>\n' +
                '\n' +
                '                        <li>\n' +
                '                            <a href="/App/logout/"><span>注销</span></a>\n' +
                '                        </li>')
            $li.appendTo($('.user'))
        }
        else {
            var $li = $('<li>\n' +
                '                            <a href="/App/register/">注册</a>\n' +
                '                        </li>\n' +
                '                        <li>\n' +
                '                            <a href="/App/login/">登陆</a>\n' +
                '                        </li>')
            $li.appendTo($('.user'))
        }
    })


    $(".btn_search").click(function () {
        var city = $("#city_tag").text()
        var region = $("#region_tag").text()
        var min_p = $("#min_p").val()
        var max_p = $("#max_p").val()

        if (min_p.trim() == "") {
            min_p = "0"
        }
        if (max_p.trim() == "") {
            max_p = "9999999"
        }


        console.log(city, region, min_p, max_p)
        window.open("/App/search/" + city.trim() + "/" + region.trim() + "/" + min_p + "/" + max_p + "/", target = "_self")

    })

})

function choose_c(obj) {
    $('#region_tag').html("区域" + '&nbsp;<span class="caret">')
    var city_name = $(obj)
    console.log(city_name.text())
    // console.log(city_name.parent().parent().prev().text())
    var tag = city_name.parent().parent().prev()
    tag.html(city_name.text() + '&nbsp;<span class="caret">')

    $.getJSON("/App/load_region/", {"city_name": city_name.text()}, function (data) {
        var regions_list = data.regions_list
        $('.region').empty()
        for (i = 0; i < regions_list.length; i++) {
            var $li = $('<li><a href="#" class="choose_region" onclick="choose_r(this)">' + regions_list[i] + '</a></li>')

            $li.appendTo($('.region'))
        }

    })
}

function choose_r(obj) {
    // console.log(obj.innerText)
    var tag = document.getElementById("region_tag")
    // console.log(tag.innerText)
    tag.innerHTML = obj.innerText + '&nbsp;<span class="caret">'
}

