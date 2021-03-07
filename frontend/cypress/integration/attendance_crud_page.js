import decodeJwt from 'jwt-decode';

describe('The Attendance', () => {
  before(() => {
    cy.request({
      method: 'POST',
      url: 'http://localhost:8000/api/token',
      form: true, //sets to application/x-www-form-urlencoded
      body: {
        username: 'admin@posgrad.com',
        password: '123456',
      },
    }).then((response) => {
      const decodedToken = decodeJwt(response.body.access_token);
      localStorage.setItem('token', response.body.access_token);
      localStorage.setItem('permissions', decodedToken.permissions);
      cy.request({
        method: 'POST',
        url: 'http://localhost:8000/api/v1/contato',
        body: {
          email: 'ppgp@example.com',
          location: 'Nepsa 2',
          schedule: '8:30 as 18:30',
          owner_id: 1,
        },
        headers: {
          authorization: `Bearer ${response.body.access_token}`,
        },
      });
    });
  });

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

  it('Check attendance exists', () => {
    cy.visit('/admin#/contato');
    cy.get('#main-content').should('contain', 'ppgp@example.com');
    cy.get('#main-content').should('contain', 'Nepsa 2');
    cy.get('#main-content').should('contain', '8:30 as 18:30');
  });

  it('Edit attendance', () => {
    cy.visit('/admin#/contato');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#email').clear().type('ppgp@ccsa.ufrn.br');
    cy.get('#location').clear().type('Nepsa 1');
    cy.get('#schedule').clear().type('Horarios novos');
    cy.get('[aria-label="Save"]').click();
    cy.get('#main-content').should('contain', 'ppgp@ccsa.ufrn.br');
    cy.get('#main-content').should('contain', 'Nepsa 1');
    cy.get('#main-content').should('contain', 'Horarios novos');
  });
});
