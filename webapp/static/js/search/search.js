$(function () {
    $.getJSON("/App/searchinfo/", function (data) {
        var regions_list = data.regions_list
        $('.region').empty()
        for (i = 0; i < regions_list.length; i++) {
            var $li = $('<li><a href="#" class="choose_region" onclick="choose_r(this)">' + regions_list[i] + '</a></li>')

            $li.appendTo($('.region'))
        }
        $("#city_tag").html(data.city + '&nbsp;<span class="caret">')
        $("#region_tag").html(data.region + '&nbsp;<span class="caret">')
        $("#min_p").val(data.min_p)
        $("#max_p").val(data.max_p)

        $('.features').each(function () {
            var content = $(this).text()
            if (content.length > 22) {
                var newcontent = content.substr(0, 22) + '...'
                console.log(newcontent)
                $(this).text(newcontent)
            } else {
                // $(this).html(content + '随时看房,拎包入住..  ')
            }

        })

    })
})