import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AuthProvider from './provider/AuthProvider'
// import './App.css'
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Footer from './components/Footer';
import Login from './pages/auth/Login';
import CategoryPage from './pages/Category';
import ProductPage from './pages/Product';
import CartPage from './pages/users/Cart';
import RegisterPage from './pages/auth/Register';
import ProfilePage from './pages/users/Profile';
import OrderPage from './pages/users/Order';
import CheckoutForm from './pages/Checkout';
import OrderInfo from './pages/users/OrderInfo';


function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/category/:slug" element={<CategoryPage />} />
          <Route path='/product/:slug' element={<ProductPage />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<RegisterPage />} />
          <Route path='/' element={<Home />} />
          <Route path='/checkout' element={<CheckoutForm />} />
          <Route path='/user/orderinfo/:id' element={
            <AuthProvider>
              <OrderInfo />
            </AuthProvider>
          } />
          <Route path='/user/cart' element={
            <AuthProvider>
              <CartPage />

            </AuthProvider>}
          />

          <Route path='/user/profile' element={
            <AuthProvider>
              <ProfilePage />
            </AuthProvider>
          } />


          <Route path='/user/order' element={
            <AuthProvider>
              <OrderPage />
            </AuthProvider>
          } />




          {/* <Route path='/user' element={<AuthProvider />}>
            <Route index element={<h1>Hello Profile</h1>} />
            <Route path='profile' element={<ProfilePage />} />
          </Route> */}

          <Route path='*' element={<h1>No</h1>} />
        </Routes>
        <br />
        <br />
        <br />
        <Footer />
      </BrowserRouter>
    </div>
  )
}

export default App;