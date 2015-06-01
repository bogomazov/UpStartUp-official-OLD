'use strict';

import MainCtrl from './main/main.controller';
// Navbar
import NavbarCtrl from '../app/components/navbar/navbar.controller';
// Login
import LoginFormDirective from '../app/components/login/login.directive';
import LoginService from '../app/components/login/login.service';
// Registration
import RegistrationCtrl from '../app/components/registration/registration.controller';
import RegistrationFormDirective from '../app/components/registration/registration.directive';
import RegistrationService from '../app/components/registration/registration.service';

angular.module('upStartUp', ['ngAnimate', 'ngCookies', 'ngTouch',
    'ngSanitize', 'ngResource', 'ngRoute'
  ])
  .controller('MainCtrl', MainCtrl)
  // Navbar
  .controller('NavbarCtrl', NavbarCtrl)
  // Login
  .directive('loginForm', () => new LoginFormDirective())
  .service('LoginService', LoginService)
  // Registration
  .controller('RegistrationCtrl', RegistrationCtrl)
  .directive('registrationForm', () => new RegistrationFormDirective())
  .service('RegistrationService', RegistrationService)

.config(function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'app/main/main.html',
      controller: 'MainCtrl'
    })
    .when('/registration', {
      templateUrl: 'app/components/registration/registration.html',
      controller: 'RegistrationCtrl'
    })
    .otherwise({
      redirectTo: '/'
    });

  $locationProvider.html5Mode(true);
});
