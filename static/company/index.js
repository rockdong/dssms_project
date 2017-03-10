/**
 * Created by rockdong on 2017/2/10.
 */

'use strict';

var menuApp = angular.module('menuApp', []);

// menuApp.run(function () {
//     angular.element("nav > ul.nav > li > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//     // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
//     angular.element("nav > ul.nav > li > a:only-child").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//
//     // 给每个一可点击跳转的菜单加载方法
//     // 当前节点下有子节点
//     angular.element("div[class='dropdown-menu wrapper w-full bg-white'] > div > div > div.row > div > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
// });


// $(function () {
//     // 给每个一可点击跳转的菜单加载方法
//     // 当前节点下有子节点
//     $("nav > ul.nav > li > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//     // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
//     $("nav > ul.nav > li > a:only-child").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//
//     // 给每个一可点击跳转的菜单加载方法
//     // 当前节点下有子节点
//     $("div[class='dropdown-menu wrapper w-full bg-white'] > div > div > div.row > div > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//     // // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
//     // $("nav > ul.nav > li > a:only-child").bind('click', function () {
//     //     getHtmlCode($(this).attr("name"));
//     // });
//
// });


// $(function () {
//     // 给每个一可点击跳转的菜单加载方法
//     // 当前节点下有子节点
//     $("nav > ul.nav > li > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//     // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
//     $("nav > ul.nav > li > a:only-child").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//
//     // 给每个一可点击跳转的菜单加载方法
//     // 当前节点下有子节点
//     $("div[class='dropdown-menu wrapper w-full bg-white'] > div > div > div.row > div > ul > li > a[href='#']").bind('click', function () {
//         getHtmlCode($(this).attr("name"));
//     });
//     // // 如果当前节点下面没有 ul 子节点，说明菜单项中没有子项
//     // $("nav > ul.nav > li > a:only-child").bind('click', function () {
//     //     getHtmlCode($(this).attr("name"));
//     // });
//
// });

// function getHtmlCode(value) {
//     $("#content").html("");
//     $("#content").load('/index/' + value);
// }