import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';

export const placeOrder = createAsyncThunk(
  'order/placeOrder',
  async (orderData, { rejectWithValue, getState }) => {
    try {
      const accessToken = getState().loginReducer.accessToken;

      if (!accessToken) {
        console.error('accessToken is null');
        return rejectWithValue('accessToken is null');
      }

      const response = await myApi.post(
        '/order/create-order-place',
        orderData,
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );

      return response.data;
    } catch (error) {
      console.log(error.response.data);
      return rejectWithValue(error.response.data);
    }
  }
);

export const getOrdersByUserId = createAsyncThunk(
  'order/getOrdersByUserId',
  async (_, { rejectWithValue, getState }) => {
    try {
      const accessToken = getState().loginReducer.accessToken;

      if (!accessToken) {
        console.error('accessToken is null');
        return rejectWithValue('accessToken is null');
      }
      //
      const response = await myApi.get(`/order/get-order-by-user`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const getOrderById = createAsyncThunk(
  'order/getOrderById',
  async (id, { getState, rejectWithValue }) => {
    try {
      const accessToken = getState().loginReducer.accessToken;

      if (!accessToken) {
        console.error('accessToken is null');
        return rejectWithValue('accessToken is null');
      }

      const response = await myApi.get(`/order/get-order-by-id/${id}`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const getAllOrders = createAsyncThunk(
  'order/getAllOrders',
  async (_, { rejectWithValue, getState }) => {
    try {
      const accessToken = getState().loginReducer.accessToken;

      if (!accessToken) {
        console.error('accessToken is null');
        return rejectWithValue('accessToken is null');
      }

      const response = await myApi.get('/order', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const orderSlice = createSlice({
  name: 'order',
  initialState: {
    placeOrderLoading: false,
    placeOrderSuccess: false,
    placeOrderError: false,
    getOrdersByUserIdLoading: false,
    getOrdersByUserIdError: false,
    getOrderByIdLoading: false,
    getOrderByIdError: false,
    getAllOrdersLoading: false,
    getAllOrdersError: false,
    orders: [],
    order: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(placeOrder.pending, (state) => {
        state.placeOrderLoading = true;
        state.placeOrderSuccess = false;
        state.placeOrderError = false;
      })
      .addCase(placeOrder.fulfilled, (state) => {
        state.placeOrderLoading = false;
        state.placeOrderSuccess = true;
        state.placeOrderError = false;
      })
      .addCase(placeOrder.rejected, (state) => {
        state.placeOrderLoading = false;
        state.placeOrderSuccess = false;
        state.placeOrderError = true;
      })
      .addCase(getOrdersByUserId.pending, (state) => {
        state.getOrdersByUserIdLoading = true;
        state.getOrdersByUserIdError = false;
      })
      .addCase(getOrdersByUserId.fulfilled, (state, action) => {
        state.getOrdersByUserIdLoading = false;
        state.getOrdersByUserIdError = false;
        state.orders = action.payload;
      })
      .addCase(getOrdersByUserId.rejected, (state) => {
        state.getOrdersByUserIdLoading = false;
        state.getOrdersByUserIdError = true;
      })
      .addCase(getOrderById.pending, (state) => {
        state.getOrderByIdLoading = true;
        state.getOrderByIdError = false;
      })
      .addCase(getOrderById.fulfilled, (state, action) => {
        state.getOrderByIdLoading = false;
        state.getOrderByIdError = false;
        state.order = action.payload;
      })
      .addCase(getOrderById.rejected, (state) => {
        state.getOrderByIdLoading = false;
        state.getOrderByIdError = true;
      })
      .addCase(getAllOrders.pending, (state) => {
        state.getAllOrdersLoading = true;
        state.getAllOrdersError = false;
      })
      .addCase(getAllOrders.fulfilled, (state, action) => {
        state.getAllOrdersLoading = false;
        state.getAllOrdersError = false;
        state.orders = action.payload;
      })
      .addCase(getAllOrders.rejected, (state) => {
        state.getAllOrdersLoading = false;
        state.getAllOrdersError = true;
      });
  },
});

export default orderSlice.reducer;
