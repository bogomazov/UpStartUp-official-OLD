'use strict';

import RegistrationCtrl from './registration.controller';

class RegistrationFormDirective {
  constructor() {
    this.restrict = 'E';
    this.controller = RegistrationCtrl;
    this.templateUrl = '../app/components/registration/registration.directive.html';
  }
}

export default RegistrationFormDirective;
