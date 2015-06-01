'use strict';

class RegistrationCtrl {
  constructor($scope, RegistrationService) {

    $scope.checkRegistration = function(user) {
      RegistrationService.checkUserRegistration(angular.copy(user))
        .success(function(data) {
          console.log(data);
        });
    };

  }
}

RegistrationCtrl.$inject = ['$scope', 'RegistrationService'];

export default RegistrationCtrl;
