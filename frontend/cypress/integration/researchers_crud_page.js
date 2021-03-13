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

  it('Add researcher', () => {
	cy.intercept('POST', 'pesquisador').as('addResearcher');
    cy.visit('/admin#/pesquisador/create');
    cy.get('#cpf').type('123456789');
    cy.get('#name').type('Luccas Mateus de Medeiros Gomes');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@addResearcher');
    cy.visit('/admin#/pesquisador');
    cy.get('[href*="#/pesquisador"]').first().click();
    cy.get('#main-content').should('contain', '123456789');
    cy.get('#main-content').should(
      'contain',
      'Luccas Mateus de Medeiros Gomes'
    );
  });

  it('List researchers', () => {
	cy.intercept('GET', 'pesquisador').as('getResearchers');
    cy.visit('/admin#/pesquisador');
	cy.wait('@getResearchers');
    cy.get('[href*="#/pesquisador"]').first().click();
    cy.get('#main-content').should('contain', '123456789');
    cy.get('#main-content').should(
      'contain',
      'Luccas Mateus de Medeiros Gomes'
    );
  });

  it('Edit researcher', () => {
	cy.intercept('PUT', 'pesquisador').as('editResearcher');
    cy.visit('/admin#/pesquisador');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#cpf').clear().type('987654321');
    cy.get('#name').clear().type('Leticia Gabriela de Medeiros Gomes');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@editResearcher');
    cy.get('[href*="#/pesquisador"]').first().click();
    cy.get('#main-content').should('contain', '987654321');
    cy.get('#main-content').should(
      'contain',
      'Leticia Gabriela de Medeiros Gomes'
    );
  });

  it('Delete researcher', () => {
	cy.intercept('DELETE', 'pesquisador').as('deleteResearcher');
    cy.visit('/admin#/pesquisador');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
	cy.wait('@deleteResearcher');
    cy.visit('/admin#/pesquisador');
    cy.get('[href*="#/pesquisador"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
