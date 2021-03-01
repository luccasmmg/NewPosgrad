describe('The Login Page for admin', () => {
  it('Successfully loads', () => {
    cy.visit('/login');
    cy.contains('Login');
  });

  it('sets auth cookie when logging in via', () => {
    cy.visit('/login');

    cy.get('input[type=email]').type('teste@posgrad.com');
    cy.get('input[type=password]').type(`123456`);
    cy.get('#login-button').click();

    cy.url().should('include', '/admin');
  });
});
