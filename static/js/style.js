$(function () {
    var color="";
    $("tr").mouseenter(function () {
        color=$(this).css("background-color");
        $(this).css("background-color","#D9EDF7");
    });
    $("tr").mouseleave(function () {
        $(this).css("background-color",color);
    });

});
