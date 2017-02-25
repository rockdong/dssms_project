/**
 * Created by rockdong on 2017/2/20.
 */

var mainApp = angular.module('mainApp', [
    'ngRoute',
    'helloWorldControllers'
]);

angular.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider.
                when('/all_staff', {
                    templateUrl: 'partials/main.html',
                    controller: 'MainCtrl'
                }).when('/show', {
                    templateUrl: 'partials/show.html',
                    controller: 'ShowCtrl'
                });

        $locationProvider.html5Mode(false).hashPrefix('!');
    }]);