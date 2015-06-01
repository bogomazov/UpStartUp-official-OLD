'use strict';

class LoginCtrl {
  constructor($scope, LoginService) {

    $scope.checkLogin = function(user) {
      LoginService.checkUserAuthentication(angular.copy(user))
      .success(function(data) {
      console.log(data);
      });
    };

  }
}

LoginCtrl.$inject = ['$scope', 'LoginService'];

export default LoginCtrl;
