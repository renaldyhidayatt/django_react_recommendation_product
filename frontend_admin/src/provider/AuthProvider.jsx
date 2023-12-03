import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateTokenAsync } from '@/redux/auth';
import { Navigate } from 'react-router-dom';

const AuthProvider = ({ children }) => {
  const dispatch = useDispatch();
  const refreshToken = useSelector((state) => state.loginReducer.refreshToken);

  if (!refreshToken) {
    return <Navigate to={'/'} />;
  }

  useEffect(() => {
    const refreshInterval = setInterval(() => {
      dispatch(updateTokenAsync());
    }, 1000 * 60 * 4); // Panggil dispatch setiap 4 menit

    return () => clearInterval(refreshInterval);
  }, [dispatch]);

  return refreshToken ? children : <Navigate to={'/'} />;
};

export default AuthProvider;