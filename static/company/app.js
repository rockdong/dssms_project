/**
 * Created by rockdong on 2017/2/15.
 */

var staffsApp = angular.module('staffsApp', []);

staffsApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

staffsApp.run(function () {
    alert("hello");
});

staffsApp.controller('staffsCtrl', function ($scope) {
    $scope.sayHello = function () {
        alert("hello");
    }
});