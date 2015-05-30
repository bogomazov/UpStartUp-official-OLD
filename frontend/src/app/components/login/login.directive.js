'use strict';

import LoginCtrl from './login.controller';

class LoginFormDirective {
  constructor() {
    this.restrict = 'E';
    this.controller = LoginCtrl;
    this.templateUrl = '../app/components/login/login.html';
  }
}

export default LoginFormDirective;
