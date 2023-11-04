import React from 'react';
import Sidebar from './Sidebar';
import '../scss/app.scss';
import '../scss/iconly.scss';
import '../scss/pages/auth.scss';
import '../scss/themes/dark/app-dark.scss';
import AuthProvider from '@/provider/AuthProvider';
import Modal from '@/helpers/modal';

export default function LayoutAdmin({ children }) {
  return (
    <AuthProvider>
      <div id="app">
        <div id="sidebar" className="active sidebar-desktop">
          <Sidebar />
        </div>
        <div id="main">
          <header className="mb-3">
            <a href="#" className="burger-btn d-block d-xl-none">
              <i className="bi bi-justify fs-3"></i>
            </a>
          </header>
          {children}
          <Modal />
        </div>
      </div>
    </AuthProvider>
  );
}
