// Navbar.js

import React from 'react';
import { Nav, Navbar as BootstrapNavbar } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import ProfileMenu from '../components/profileMenu';
import { useRouter } from 'next/navigation';

const Navbar = () => {
  const router = useRouter();

  return (
    <BootstrapNavbar bg="white" expand="lg" className="shadow">
      <div className="container">
        <LinkContainer to="/">
          <BootstrapNavbar.Brand>
            {/* Assuming Logo is a component */}
            <Logo />
          </BootstrapNavbar.Brand>
        </LinkContainer>
        <BootstrapNavbar.Toggle aria-controls="basic-navbar-nav" />
        <BootstrapNavbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <LinkContainer to="/">
              <Nav.Link>Home</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/categories">
              <Nav.Link className={router.pathname === '/categories' ? 'active' : ''}>Categories</Nav.Link>
            </LinkContainer>
            {localStorage.getItem("LogedIn") && (
              <LinkContainer to="/cart">
                <Nav.Link>My Cart</Nav.Link>
              </LinkContainer>
            )}
          </Nav>
          <Nav>
            {localStorage.getItem("LogedIn") ? (
              <div className='mt-1'>
                <ProfileMenu />
              </div>
            ) : (
              <LinkContainer to='/login'>
                <Nav.Link>Login</Nav.Link>
              </LinkContainer>
            )}
          </Nav>
        </BootstrapNavbar.Collapse>
      </div>
    </BootstrapNavbar>
  );
};

export default Navbar;
