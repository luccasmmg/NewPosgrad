import decodeJwt from 'jwt-decode';

describe('Participation CRUD', () => {
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

  it('Add participation', () => {
    cy.visit('/admin#/participacao/create');
    cy.get('#title').type('Participacao');
    cy.get('#description').type('Descricao teste');
    cy.get('#year').type('2021');
    cy.get('#international').click();
    cy.get('[aria-label="Save"]').click();
    cy.visit('/admin#/participacao');
    cy.get('#main-content').should('contain', 'Participacao');
    cy.get('#main-content').should('contain', 'Descricao teste');
    cy.get('#main-content').should('contain', '2021');
    cy.get('[title="Yes"]').should('exist');
  });

  it('List participations', () => {
    cy.visit('/admin#/participacao');
    cy.get('#main-content').should('contain', 'Participacao');
    cy.get('#main-content').should('contain', 'Descricao teste');
    cy.get('#main-content').should('contain', '2021');
    cy.get('[title="Yes"]').should('exist');
  });

  it('Edit participation', () => {
    cy.visit('/admin#/participacao');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#title').clear().type('Participacao 2');
    cy.get('#description').clear().type('Descricao teste 2');
    cy.get('#international').click();
    cy.get('[aria-label="Save"]').click();
    cy.get('#main-content').should('contain', 'Participacao 2');
    cy.get('#main-content').should('contain', 'Descricao teste 2');
    cy.get('#main-content').should('contain', '2021');
    cy.get('[title="No"]').should('exist');
  });

  it('Delete participation', () => {
    cy.visit('/admin#/participacao');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
    cy.visit('/admin#/participacao');
    cy.get('[href*="#/participacao"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
