import decodeJwt from 'jwt-decode';

describe('Event CRUD', () => {
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

  it('Add event', () => {
	cy.intercept('POST', 'evento').as('addEvent');
    cy.visit('/admin#/evento/create');
    cy.get('#title').type('Titulo');
    cy.get('#link').type('https://google.com');
    cy.get('#initial_date').type('2020-07-15T18:00');
    cy.get('#final_date').type('2020-07-16T18:00');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@addEvent');
    cy.visit('/admin#/evento');
    cy.get('#main-content').should('contain', 'Titulo');
    cy.get('#main-content').should('contain', 'https://google.com');
    cy.get('#main-content').should('contain', '15/07/2020 18:00:00');
    cy.get('#main-content').should('contain', '16/07/2020 18:00:00');
  });

  it('List events', () => {
	cy.intercept('GET', 'evento').as('getEvents');
    cy.visit('/admin#/evento');
	cy.wait('@getEvents');
    cy.get('#main-content').should('contain', 'Titulo');
    cy.get('#main-content').should('contain', 'https://google.com');
    cy.get('#main-content').should('contain', '15/07/2020 18:00:00');
    cy.get('#main-content').should('contain', '16/07/2020 18:00:00');
  });

  it('Edit event', () => {
	cy.intercept('PUT', 'evento').as('editEvents');
    cy.visit('/admin#/evento');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('#title').clear().type('Titulo 2');
    cy.get('#link').clear().type('https://duckduckgo.com');
    cy.get('#initial_date').clear().type('2020-07-15T19:00');
    cy.get('#final_date').clear().type('2020-07-16T20:00');
    cy.get('[aria-label="Save"]').click();
	cy.wait('@editEvents');
    cy.get('#main-content').should('contain', 'Titulo 2');
    cy.get('#main-content').should('contain', 'https://duckduckgo.com');
    cy.get('#main-content').should('contain', '15/07/2020 19:00:00');
    cy.get('#main-content').should('contain', '16/07/2020 20:00:00');
  });

  it('Delete event', () => {
	cy.intercept('DELETE', 'evento').as('deleteEvents');
    cy.visit('/admin#/evento');
    cy.get('[aria-label="Edit"]').first().click();
    cy.get('[aria-label="Delete"]').click();
	cy.wait('@deleteEvents');
    cy.visit('/admin#/evento');
    cy.get('[href*="#/evento"]').first().click();
    cy.get('div[class^="RaEmpty-message-"]').should('exist');
  });
});
