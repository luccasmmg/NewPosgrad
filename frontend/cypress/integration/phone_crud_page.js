import decodeJwt from 'jwt-decode';

describe('Phone CRUD', () => {
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

  it('Add phone', () => {
	cy.intercept('POST', 'telefone').as('addPhone');
    cy.visit('/admin#/telefone/create');
    cy.get('#number').type('123456');
    cy.get('#phone_type').click();
    cy.get('[data-value="cellphone"]').click();
    cy.get('[aria-label="Save"]').click();
	cy.wait('@addPhone');
    cy.visit('/admin#/telefone');
    cy.get('[href*="#/telefone"]').first().click();
    cy.get('#main-content').should('contain', '123456');
    cy.get('#main-content').should('contain', 'Celular');
  });

  it('List participations', () => {
	cy.intercept('GET', 'telefone').as('getPhones');
    cy.visit('/admin#/telefone');
	cy.wait('@getPhones');
    cy.get('[href*="#/telefone"]').first().click();
    cy.get('#main-content').should('contain', '123456');
    cy.get('#main-content').should('contain', 'Celular');
  });

  it('Edit phone', () => {
	cy.intercept('PUT', 'telefone').as('editPhone');
    cy.visit('/admin#/telefone');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#number').clear().type('134');
    cy.get('#phone_type').click();
    cy.get('[data-value="fixed"]').click();
    cy.get('[aria-label="Save"]').click();
	cy.wait('@editPhone');
    cy.get('[href*="#/telefone"]').first().click();
    cy.get('#main-content').should('contain', '134');
    cy.get('#main-content').should('contain', 'Fixo');
  });

  it('Delete phone', () => {
	cy.intercept('DELETE', 'telefone').as('deletePhone');
    cy.visit('/admin#/telefone');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
	cy.wait('@deletePhone');
    cy.visit('/admin#/telefone');
    cy.get('[href*="#/telefone"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
