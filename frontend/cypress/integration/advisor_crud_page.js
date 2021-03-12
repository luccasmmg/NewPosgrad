import decodeJwt from 'jwt-decode';

describe('The Student advisor CRUD', () => {
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

  it('Add student advisor', () => {
	cy.intercept('POST', 'coordenador').as('addAdvisor');
    cy.visit('/admin#/coordenador/create');
    cy.get('#registration').type('123456789');
    cy.get('#advisor_name').type('Luccas Mateus de Medeiros Gomes');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@addAdvisor');
    cy.visit('/admin#/coordenador');
    cy.get('#main-content').should('contain', '123456789');
    cy.get('#main-content').should(
      'contain',
      'Luccas Mateus de Medeiros Gomes'
    );
  });

  it('List student advisors', () => {
	cy.intercept('GET', 'coordenador').as('getAdvisors');
    cy.visit('/admin#/coordenador');
	cy.wait('@getAdvisors');
    cy.get('#main-content').should('contain', '123456789');
    cy.get('#main-content').should(
      'contain',
      'Luccas Mateus de Medeiros Gomes'
    );
  });

  it('Edit student advisor', () => {
	cy.intercept('PUT', 'coordenador').as('editAdvisor');
    cy.visit('/admin#/coordenador');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#registration').clear().type('987654321');
    cy.get('#advisor_name').clear().type('Leticia Gabriela de Medeiros Gomes');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@editAdvisor');
    cy.get('#main-content').should('contain', '987654321');
    cy.get('#main-content').should(
      'contain',
      'Leticia Gabriela de Medeiros Gomes'
    );
  });

  it('Delete student advisor', () => {
	cy.intercept('DELETE', 'coordenador').as('deleteAdvisor');
    cy.visit('/admin#/coordenador');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
	cy.wait('@deleteAdvisor');
    cy.visit('/admin#/coordenador');
    cy.get('[href*="#/coordenador"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
