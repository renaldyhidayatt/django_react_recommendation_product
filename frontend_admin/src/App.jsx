import LayoutAdmin from '@/components/LayoutAdmin';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import LayoutAuth from './components/LayoutAuth';
import RegisterPage from './pages/auth/Register';
import LoginPage from './pages/auth/Login';
import CategoryPage from './pages/admin/category';
import EditCategoryPage from './pages/admin/category/edit';
import ProductPage from './pages/admin/product';
import EditProductPage from './pages/admin/product/edit';
import OrderPage from './pages/admin/order';
import SliderPage from './pages/admin/slider';
import EditSliderPage from './pages/admin/slider/edit';
import UserPage from './pages/admin/user';
import EditUserPage from './pages/admin/user/edit';
import Dashboard from './pages/admin/Dashboard';

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route
            path="/admin/category"
            element={
              <LayoutAdmin>
                <CategoryPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/category/edit/:id"
            element={
              <LayoutAdmin>
                <EditCategoryPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/product"
            element={
              <LayoutAdmin>
                <ProductPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/product/edit/:id"
            element={
              <LayoutAdmin>
                <EditProductPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/order"
            element={
              <LayoutAdmin>
                <OrderPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/slider"
            element={
              <LayoutAdmin>
                <SliderPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/slider/edit/:id"
            element={
              <LayoutAdmin>
                <EditSliderPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/user"
            element={
              <LayoutAdmin>
                <UserPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin/user/edit/:id"
            element={
              <LayoutAdmin>
                <EditUserPage />
              </LayoutAdmin>
            }
          />
          <Route
            path="/admin"
            element={
              <LayoutAdmin>
                <Dashboard />
              </LayoutAdmin>
            }
          />

          <Route
            path="/"
            element={
              <LayoutAuth>
                <LoginPage />
              </LayoutAuth>
            }
          />
          <Route
            path="/register"
            element={
              <LayoutAuth>
                <RegisterPage />
              </LayoutAuth>
            }
          />
        </Routes>
      </BrowserRouter>
    </>
  );
}
