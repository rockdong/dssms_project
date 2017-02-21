/**
 * Created by rockdong on 2017/2/19.
 */

var loginController = angular.module('loginController', []);



loginController.controller('loginCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.login = function () {
        $http.get('login/').then(function () {
            // success
            alert('success');
        }, function () {
            // field
            alert('field');
        });
    }
}]);