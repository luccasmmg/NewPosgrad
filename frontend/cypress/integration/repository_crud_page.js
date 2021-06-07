import decodeJwt from 'jwt-decode';

describe('Repository CRUD', () => {
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

  it('Add repository document', () => {
    cy.intercept('POST', 'repositorio').as('addRepositoryDocs');
    cy.visit('/admin#/repositorio/create');
    cy.get('#title').type('Repositorio');
    cy.get('#author').type('Luccas Mateus');
    cy.get('#year').type('2021');
    cy.get('#link').type('https://google.com.br');
    cy.get('[aria-label="Save"]').click();
    cy.wait('@addRepositoryDocs');
    cy.visit('/admin#/repositorio');
    cy.get('[href*="#/repositorio"]').first().click();
    cy.get('#main-content').should('contain', 'Repositorio');
    cy.get('#main-content').should('contain', 'Luccas Mateus');
    cy.get('#main-content').should('contain', '2021');
    cy.get('#main-content').should('contain', 'https://google.com.br');
  });

  it('List participations', () => {
    cy.intercept('GET', 'repositorio').as('getRespositoryDocs');
    cy.visit('/admin#/repositorio');
    cy.wait('@getRespositoryDocs');
    cy.get('[href*="#/repositorio"]').first().click();
    cy.get('#main-content').should('contain', 'Repositorio');
    cy.get('#main-content').should('contain', 'Luccas Mateus');
    cy.get('#main-content').should('contain', '2021');
    cy.get('#main-content').should('contain', 'https://google.com.br');
  });

  it('Edit repository document', () => {
    cy.intercept('PUT', 'repositorio').as('editRepositoryDocs');
    cy.visit('/admin#/repositorio');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#title').clear().type('Repositorio 2');
    cy.get('#author').clear().type('Luccas Mateus 2');
    cy.get('[aria-label="Save"]').click();
    cy.wait('@editRepositoryDocs');
    cy.get('[href*="#/repositorio"]').first().click();
    cy.get('#main-content').should('contain', 'Repositorio 2');
    cy.get('#main-content').should('contain', 'Luccas Mateus 2');
    cy.get('#main-content').should('contain', '2021');
    cy.get('#main-content').should('contain', 'https://google.com.br');
  });

  it('Delete repository document', () => {
    cy.intercept('DELETE', 'repositorio').as('deleteRepositoryDocs');
    cy.visit('/admin#/repositorio');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
    cy.wait('@deleteRepositoryDocs');
    cy.visit('/admin#/repositorio');
    cy.get('[href*="#/repositorio"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
