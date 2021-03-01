describe('The Login Page for admin', () => {
  it('Successfully loads', () => {
    cy.visit('/login');
    cy.contains('Login');
  });

  it('sets local storage when logging in', () => {
    cy.visit('/login');

    cy.get('input[type=email]').type('teste@posgrad.com');
    cy.get('input[type=password]').type(`123456`);
    cy.get('#login-button').click();

    cy.url().should('include', '/admin');
    cy.getLocalStorage('token').should('not.equal', null);
    cy.getLocalStorage('permissions').should('not.equal', null);
  });
  it('not set local storage when logging in with wrong credentials', () => {
    cy.visit('/login');

    cy.get('input[type=email]').type('teste@posgrad.com');
    cy.get('input[type=password]').type(`1234567`);
    cy.get('#login-button').click();

    cy.url().should('not.include', '/admin');
    cy.getLocalStorage('token').should('equal', null);
    cy.getLocalStorage('permissions').should('equal', null);
  });
});
