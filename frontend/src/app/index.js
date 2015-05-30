'use strict';

import MainCtrl from './main/main.controller';
import NavbarCtrl from '../app/components/navbar/navbar.controller';
import LoginFormDirective from '../app/components/login/login.directive';
import LoginService from '../app/components/login/login.service';

angular.module('upStartUp', ['ngAnimate', 'ngCookies', 'ngTouch',
    'ngSanitize', 'ngResource', 'ngRoute'
  ])
  .controller('MainCtrl', MainCtrl)
  .controller('NavbarCtrl', NavbarCtrl)
  .directive('loginForm', () => new LoginFormDirective())
  .service('LoginService', LoginService)

.config(function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'app/main/main.html',
      controller: 'MainCtrl'
    })
    .otherwise({
      redirectTo: '/'
    });

  $locationProvider.html5Mode(true);
});
