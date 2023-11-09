import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateTokenAsync } from '../redux/auth.slice';
import { Navigate } from 'react-router-dom';

const AuthProvider = ({ children }) => {
  const dispatch = useDispatch();

  const refreshToken = useSelector((state) => state.loginReducer.refreshToken);
  const loading = useSelector((state) => state.loginReducer.loading);

  if (!refreshToken) {
    return <Navigate to={'/login'} />;
  }

  useEffect(() => {
    if (loading) {
      dispatch(updateTokenAsync());
    }

    const REFRESH_INTERVAL = 1000 * 60 * 4;
    let interval = setInterval(() => {
      if (refreshToken) {
        dispatch(updateTokenAsync());
      }
    }, REFRESH_INTERVAL);
    return () => clearInterval(interval);
  }, [refreshToken, loading, dispatch]);

  return (
    <>
      {loading ? <h1>Loading</h1> : null}
      {children}
    </>
  );
};

export default AuthProvider;
