'use strict';

class RegistrationService {
  constructor($http) {
    this.$http = $http;
  }

  checkUserRegistration(serializationRegistrationForm) {
    return this.$http.post('/api/v1/auth/registration/',
                serializationRegistrationForm)
    .success(function(data) {
      return data;
    })
    .error(function(err) {
      return err;
    });
  }
}

RegistrationService.$inject = ['$http'];

export default RegistrationService;
