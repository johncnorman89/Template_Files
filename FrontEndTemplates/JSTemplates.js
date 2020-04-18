//JS template code

//Hover
$(".weAre>div").hover(
        function () {
            $("img", this).stop(true, false).hide(1000);
            $(".descript", this).stop(true, false).show(1000);
        },
        function () {
            $("img", this).stop(true, false).show(1000);
            $(".descript", this).stop(true, false).hide(1000);
        });