import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';
import jwtDecode from 'jwt-decode';

const refreshToken = localStorage.getItem('refreshToken') || null;
const accessToken = localStorage.getItem('accessToken') || null;

const initialUser = accessToken ? jwtDecode(accessToken) : null;

export const registerAction = createAsyncThunk(
  'auth/register',
  async (registerData, { rejectWithValue }) => {
    try {
      const response = await myApi.post('/auth/register', registerData);
      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        return rejectWithValue(error.response.data);
      } else {
        return rejectWithValue('An error occurred while registering.');
      }
    }
  }
);

export const loginAction = createAsyncThunk(
  'auth/login',
  async (loginData, { rejectWithValue }) => {
    try {
      const response = await myApi.post('/auth/token', loginData);

      localStorage.setItem('accessToken', response.data.access);

      localStorage.setItem('refreshToken', response.data.refresh);

      return response.data;
    } catch (error) {
      if (error.response && error.response.data) {
        return rejectWithValue(error.response.data);
      } else {
        return rejectWithValue('An error occurred while logging in.');
      }
    }
  }
);

export const logoutUserAction = (navigate) => (dispatch) => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
  dispatch(clearAuthData());
  navigate('/login');
};

export const updateTokenAsync = createAsyncThunk(
  'auth/updateToken',
  async (_, { getState, dispatch }) => {
    try {
      const { refreshToken } = getState().authReducer;

      if (!refreshToken) {
        return;
      }

      console.log(refreshToken);

      const response = await myApi.post('/auth/refresh-token', {
        refresh: refreshToken,
      });

      const data = response.data;

      localStorage.setItem('accessToken', data);
    } catch (error) {
      throw error;
    }
  }
);

export const registerSlice = createSlice({
  name: 'register',
  initialState: { loading: false, success: false, error: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(registerAction.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(registerAction.fulfilled, (state, action) => {
        state.loading = false;
        state.success = true;
      })
      .addCase(registerAction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const loginSlice = createSlice({
  name: 'auth',
  initialState: {
    user: initialUser,
    accessToken: accessToken,
    refreshToken: refreshToken,
    loading: null,
  },
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload;
    },
    setAuthTokens: (state, action) => {
      state.authTokens = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    clearAuthData: (state) => {
      state.user = null;
      state.authTokens = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(loginAction.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loginAction.fulfilled, (state, action) => {
        state.loading = false;
        state.accessToken = action.payload.access;
        state.refreshToken = action.payload.refresh;

        state.user = jwtDecode(action.payload.access);
      })
      .addCase(loginAction.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const { setUser, setAuthTokens, setLoading, clearAuthData } =
  loginSlice.actions;

export default {
  setUser: setUser,
  setAuthTokens: setAuthTokens,
  setLoading: setLoading,
  clearAuthData: clearAuthData,
  loginSlice: loginSlice.reducer,
  registerSlice: registerSlice.reducer,
};
