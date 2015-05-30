'use strict';

class NavbarCtrl {
  constructor ($scope, $interval) {
    $scope.dateIterator = new Date();

    $interval(function() {
      $scope.dateIterator = new Date();
    }, 1000);
  }
}

NavbarCtrl.$inject = ['$scope', '$interval'];

export default NavbarCtrl;
