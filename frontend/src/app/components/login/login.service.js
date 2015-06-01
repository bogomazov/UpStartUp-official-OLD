'use strict';

class LoginService {
  constructor($http) {
    this.$http = $http;
  }

  checkUserAuthentication(serializationLoginForm) {
    return this.$http.post('/api/v1/auth/login/',
                serializationLoginForm)
    .success(function(data) {
      return data;
    })
    .error(function(err) {
      return err;
    });
  }
}

LoginService.$inject = ['$http'];

export default LoginService;
