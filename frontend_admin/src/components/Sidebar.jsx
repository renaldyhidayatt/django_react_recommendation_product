import { logoutUserAction } from '@/redux/auth';
import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';

const THEME_KEY = 'theme';

const isDesktop = window.innerWidth > 1200;

const calculateChildrenHeight = (el, deep = false) => {
  const children = el.children;

  let height = 0;
  for (let i = 0; i < el.childElementCount; i++) {
    const child = children[i];
    height += child.querySelector('.submenu-link').clientHeight;

    if (deep && child.classList.contains('has-sub')) {
      const subsubmenu = child.querySelector('.submenu');

      if (subsubmenu.classList.contains('submenu-open')) {
        const childrenHeight = [
          ...subsubmenu.querySelectorAll('.submenu-link'),
        ].reduce((acc, curr) => acc + curr.clientHeight, 0);
        height += childrenHeight;
      }
    }
  }
  el.style.setProperty('--submenu-height', height + 'px');
  return height;
};

const Sidebar = () => {
  const dispatch = useDispatch();

  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logoutUserAction());

    navigate('/');
  };

  useEffect(() => {
    // Function to toggle dark theme
    function toggleDarkTheme() {
      setTheme(
        document.documentElement.getAttribute('data-bs-theme') === 'dark'
          ? 'light'
          : 'dark'
      );
    }

    // Function to set the theme
    function setTheme(theme, persist = false) {
      document.body.classList.add(theme);
      document.documentElement.setAttribute('data-bs-theme', theme);

      if (persist) {
        localStorage.setItem(THEME_KEY, theme);
      }
    }

    // Function to initialize the theme
    function initTheme() {
      // If the user manually set a theme, we'll load that
      const storedTheme = localStorage.getItem(THEME_KEY);
      if (storedTheme) {
        return setTheme(storedTheme);
      }

      // Detect if the user set their preferred color scheme to dark
      if (!window.matchMedia) {
        return;
      }

      // Media query to detect dark preference
      const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

      // Register change listener
      mediaQuery.addEventListener('change', (e) =>
        setTheme(e.matches ? 'dark' : 'light', true)
      );
      return setTheme(mediaQuery.matches ? 'dark' : 'light', true);
    }

    initTheme(); // Initialize the theme

    // Your existing initialization code from sidebar.js

    if (typeof PerfectScrollbar === 'function') {
      const container = document.querySelector('.sidebar-wrapper');
      const ps = new PerfectScrollbar(container, {
        wheelPropagation: false,
      });
    }

    // Check if the element exists before using it
    const activeSidebarItem = document.querySelector('.sidebar-item.active');
    if (activeSidebarItem) {
      setTimeout(() => {
        forceElementVisibility(activeSidebarItem);
      }, 300);
    }

    const toggler = document.getElementById('toggle-dark');
    const theme = localStorage.getItem(THEME_KEY);

    if (toggler) {
      toggler.checked = theme === 'dark';

      toggler.addEventListener('input', (e) => {
        setTheme(e.target.checked ? 'dark' : 'light', true);
      });
    }
  }, []);

  const forceElementVisibility = (el) => {
    const isElementInViewport = (el) => {
      if (el) {
        var rect = el.getBoundingClientRect();
        return (
          rect.top >= 0 &&
          rect.left >= 0 &&
          rect.bottom <=
          (window.innerHeight || document.documentElement.clientHeight) &&
          rect.right <=
          (window.innerWidth || document.documentElement.clientWidth)
        );
      }
      return false;
    };

    if (isElementInViewport(el)) {
      el.scrollIntoView(false);
    }
  };

  return (
    <div className={`sidebar-wrapper ${isDesktop ? 'active' : 'inactive'}`}>
      <div className="sidebar-header position-relative">
        <div className="d-flex justify-content-between align-items-center">
          <div className="logo">
            <li>
              <img
                src="/images/logo/logo.svg"
                alt="Logo"
                width={100}
                height={100}
              />
            </li>
          </div>
          <div className="theme-toggle d-flex gap-2 align-items-center mt-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              xmlnsXlink="http://www.w3.org/1999/xlink"
              aria-hidden="true"
              role="img"
              className="iconify iconify--system-uicons"
              width={20}
              height={20}
              preserveAspectRatio="xMidYMid meet"
              viewBox="0 0 21 21"
            >
              <g
                fill="none"
                fillRule="evenodd"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path
                  d="M10.5 14.5c2.219 0 4-1.763 4-3.982a4.003 4.003 0 0 0-4-4.018c-2.219 0-4 1.781-4 4c0 2.219 1.781 4 4 4zM4.136 4.136L5.55 5.55m9.9 9.9l1.414 1.414M1.5 10.5h2m14 0h2M4.135 16.863L5.55 15.45m9.899-9.9l1.414-1.415M10.5 19.5v-2m0-14v-2"
                  opacity=".3"
                />
                <g transform="translate(-210 -1)">
                  <path d="M220.5 2.5v2m6.5.5l-1.5 1.5" />
                  <circle cx="220.5" cy="11.5" r={4} />
                  <path d="m214 5l1.5 1.5m5 14v-2m6.5-.5l-1.5-1.5M214 18l1.5-1.5m-4-5h2m14 0h2" />
                </g>
              </g>
            </svg>
            <div className="form-check form-switch fs-6">
              <input
                className="form-check-input me-0"
                type="checkbox"
                id="toggle-dark"
                style={{ cursor: 'pointer' }}
              />
              <label className="form-check-label" />
            </div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              xmlnsXlink="http://www.w3.org/1999/xlink"
              aria-hidden="true"
              role="img"
              className="iconify iconify--mdi"
              width={20}
              height={20}
              preserveAspectRatio="xMidYMid meet"
              viewBox="0 0 24 24"
            >
              <path
                fill="currentColor"
                d="m17.75 4.09l-2.53 1.94l.91 3.06l-2.63-1.81l-2.63 1.81l.91-3.06l-2.53-1.94L12.44 4l1.06-3l1.06 3l3.19.09m3.5 6.91l-1.64 1.25l.59 1.98l-1.7-1.17l-1.7 1.17l.59-1.98L15.75 11l2.06-.05L18.5 9l.69 1.95l2.06.05m-2.28 4.95c.83-.08 1.72 1.1 1.19 1.85c-.32.45-.66.87-1.08 1.27C15.17 23 8.84 23 4.94 19.07c-3.91-3.9-3.91-10.24 0-14.14c.4-.4.82-.76 1.27-1.08c.75-.53 1.93.36 1.85 1.19c-.27 2.86.69 5.83 2.89 8.02a9.96 9.96 0 0 0 8.02 2.89m-1.64 2.02a12.08 12.08 0 0 1-7.8-3.47c-2.17-2.19-3.33-5-3.49-7.82c-2.81 3.14-2.7 7.96.31 10.98c3.02 3.01 7.84 3.12 10.98.31Z"
              />
            </svg>
          </div>
          <div className="sidebar-toggler x">
            <li className="sidebar-hide d-xl-none d-block">
              <i className="bi bi-x bi-middle" />
            </li>
          </div>
        </div>
      </div>
      <div className="sidebar-menu">
        <ul className="menu">
          <li className="sidebar-title">Menu</li>
          <li className="sidebar-item active">
            <Link to={'/admin'} className="sidebar-link">
              <i className="bi bi-grid-fill" />
              <span>Dashboard</span>
            </Link>
          </li>
          <li className="sidebar-item">
            <a href="https://proyekakhiranalytics-8z9rndznzsefms2wndqsne.streamlit.app/" className="sidebar-link" target="_blank" rel="noopener noreferrer">
              <i className="bi bi-grid-fill" />
              <span>Dashboard Analytics</span>
            </a>
          </li>

          <li className="sidebar-item">
            <Link to={'/admin/user'} className="sidebar-link">
              <i className="bi bi-person-fill" />
              <span>User</span>
            </Link>
          </li>
          <li className="sidebar-item ">
            <Link to={'/admin/category'} className="sidebar-link">
              <i className="bi bi-list-ul" />
              <span>Category</span>
            </Link>
          </li>
          <li className="sidebar-item ">
            <Link to={'/admin/product'} className="sidebar-link">
              <i className="bi bi-hammer" />
              <span>Product</span>
            </Link>
          </li>
          <li className="sidebar-item ">
            <Link to={'/admin/order'} className="sidebar-link">
              <i className="bi bi-cart" />
              <span>Order</span>
            </Link>
          </li>
          <li className="sidebar-item ">
            <Link to={'/admin/slider'} className="sidebar-link">
              <i className="bi bi-cast" />
              <span>Slider</span>
            </Link>
          </li>
          <li className="sidebar-title">Logout</li>
          <li className="sidebar-item ">
            <a onClick={() => handleLogout()} className="sidebar-link">
              <i className="bi bi-box-arrow-right" />
              <span>Logout</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
