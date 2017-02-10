/**
 * Created by rockdong on 2017/2/10.
 */

$(function () {
    // 给每个一可点击跳转的菜单加载方法
    // 当前节点下有子节点
    $("nav > ul.nav > li > ul > li > a").bind('click', function () {
        getHtmlCode($(this).attr("name"));
    });
    // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
    $("nav > ul.nav > li > a:only-child").bind('click', function () {
        alert("hello");
    });

});

function getHtmlCode(value) {
    $("#content").html("");
    $("#content").load(value);
}