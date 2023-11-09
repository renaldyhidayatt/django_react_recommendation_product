import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { registerAction } from '../../redux/auth.slice';
import { LoadingIndicator } from '../../components/Loading';
import { IsError } from '../../components/ISError';
import ISSuccess from '../../components/IsSuccess';
import SweetAlert from '../../components/Sweetalert';

export default function RegisterPage() {
  const registerstate = useSelector((state) => state.registerReducer);
  const navigate = useNavigate();

  const { loading, error, success, user } = registerstate;

  const [name, setName] = useState('');

  const [email, setemail] = useState('');

  const [password, setpassword] = useState('');
  const [cpassword, setcpassword] = useState('');

  const dispatch = useDispatch();

  const onSubmit = (e) => {
    e.preventDefault();

    const user = {
      name: name,
      email: email,
      password: password,
      password_confirmation: cpassword,
    };

    if (password === cpassword) {
      dispatch(registerAction(user));
    } else {
      SweetAlert.error(
        'Password not match',
        'Password tidak sama silakan ulang lagi!!!'
      );
    }
  };

  useEffect(() => {
    if (user) {
      navigate('/');
    }
  }, [user, navigate]);

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-full max-w-md mt-[-20px]">
        <div className="bg-white shadow-lg p-6 rounded-lg">
          <h2 className="text-center text-2xl font-semibold mb-6">Register</h2>
          <i className="fa fa-user-plus text-3xl mb-6 mx-auto"></i>

          {loading && <LoadingIndicator />}
          {error && <IsError error="Email Address is already registered" />}
          {success && <ISSuccess success="Your Registration is successful" />}

          <form onSubmit={onSubmit}>
            <input
              type="text"
              placeholder="name"
              className="w-full p-2 mb-4 border border-gray-300 rounded"
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
            />

            <input
              type="email"
              placeholder="Email"
              className="w-full p-2 mb-4 border border-gray-300 rounded"
              value={email}
              required
              onChange={(e) => setemail(e.target.value)}
            />

            <input
              type="password"
              placeholder="Password"
              className="w-full p-2 mb-4 border border-gray-300 rounded"
              value={password}
              required
              onChange={(e) => setpassword(e.target.value)}
            />

            <input
              type="password"
              placeholder="Confirm Password"
              className="w-full p-2 mb-4 border border-gray-300 rounded"
              value={cpassword}
              required
              onChange={(e) => setcpassword(e.target.value)}
            />

            <div className="text-right">
              <button
                type="submit"
                className="bg-blue-500 text-white px-4 py-2 rounded"
              >
                REGISTER
              </button>
            </div>
          </form>

          <Link to="/login" className="block mt-4 text-center">
            Click Here To Login
          </Link>
        </div>
      </div>
    </div>
  );
}
