import decodeJwt from 'jwt-decode';

describe('The Dashboard Page', () => {
  beforeEach(() => {
    cy.request({
      method: 'POST',
      url: 'http://localhost:8000/api/token',
      form: true, //sets to application/x-www-form-urlencoded
      body: {
        username: 'teste@posgrad.com',
        password: '123456',
      },
    }).then((response) => {
      const decodedToken = decodeJwt(response.body.access_token);
      localStorage.setItem('token', response.body.access_token);
      localStorage.setItem('permissions', decodedToken.permissions);
    });
  });

  it('logs in automatically when the local storage is set', () => {
    cy.visit('/admin');
    cy.get('.MuiButtonBase-root').should('contain', 'Pesquisadores');
  });
});
