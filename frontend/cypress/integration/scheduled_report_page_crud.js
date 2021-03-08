import decodeJwt from 'jwt-decode';

describe('Scheduled report CRUD', () => {
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

  it('Add Scheduled report', () => {
    cy.visit('/admin#/defesa/create');
    cy.get('#title').type('Titulo');
    cy.get('#author').type('Autor');
    cy.get('#location').type('Nepsa 2');
    cy.get('#datetime').type('2020-07-15T18:00');
    cy.get('[aria-label="Save"]').click();
    cy.visit('/admin#/defesa');
    cy.get('#main-content').should('contain', 'Titulo');
    cy.get('#main-content').should('contain', 'Autor');
    cy.get('#main-content').should('contain', 'Nepsa 2');
    cy.get('#main-content').should('contain', '15/07/2020 18:00:00');
  });

  it('List scheduled report', () => {
    cy.visit('/admin#/defesa');
    cy.get('#main-content').should('contain', 'Titulo');
    cy.get('#main-content').should('contain', 'Autor');
    cy.get('#main-content').should('contain', 'Nepsa 2');
    cy.get('#main-content').should('contain', '15/07/2020 18:00:00');
  });

  it('Edit Scheduled report', () => {
    cy.visit('/admin#/defesa');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#title').clear().type('Titulo 2');
    cy.get('#author').clear().type('Autor 2');
    cy.get('#location').clear().type('Nepsa 1');
    cy.get('#datetime').clear().type('2020-07-15T19:00');
    cy.get('[aria-label="Save"]').click();
    cy.get('#main-content').should('contain', 'Titulo 2');
    cy.get('#main-content').should('contain', 'Autor 2');
    cy.get('#main-content').should('contain', 'Nepsa 1');
    cy.get('#main-content').should('contain', '15/07/2020 19:00:00');
  });

  it('Delete Scheduled report', () => {
    cy.visit('/admin#/defesa');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
    cy.visit('/admin#/defesa');
    cy.get('[href*="#/defesa"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
