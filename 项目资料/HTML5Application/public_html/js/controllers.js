'use strict';

/* Controllers */

var helloWorldControllers = angular.module('helloWorldControllers', []);

helloWorldApp.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider.
                when('/main', {
                    templateUrl: 'partials/main.html',
                    controller: 'MainCtrl'
                }).when('/show', {
                    templateUrl: 'partials/show.html',
                    controller: 'ShowCtrl'
                });

        $locationProvider.html5Mode(false).hashPrefix('!');
    }]);


helloWorldControllers.controller('MainCtrl', ['$scope', '$location', '$http',
    function MainCtrl($scope, $location, $http) {
        $scope.message = "Hello World";
        
        $scope.fuck = function() {
            alert("fuck");
        }
        
        $scope.sayHello = function() {
            alert("hello");
        }
    }]);

helloWorldControllers.controller('ShowCtrl', ['$scope', '$location', '$http',
    function ShowCtrl($scope, $location, $http) {
        $scope.msg = "Show The World";
        
        $scope.fuck = function() {
            alert("fuck");
        }
        
        $scope.sayHello = function() {
            alert("hello show");
        }
    }]);