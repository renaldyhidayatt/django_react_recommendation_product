import { myApi } from '@/helpers';
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchOrdersAsync = createAsyncThunk(
  'order/fetchOrders',
  async (_, { rejectWithValue, getState }) => {
    try {
      const { accessToken } = getState().loginReducer; // Replace with your actual auth reducer key
      const response = await myApi.get('/order', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      console.log(accessToken);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const deleteOrderAsync = createAsyncThunk(
  'order/deleteOrder',
  async (orderId, { rejectWithValue, getState }) => {
    try {
      const { accessToken } = getState().loginReducer; // Replace with your actual auth reducer key
      const response = await myApi.delete(`/order/delete/${orderId}`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      return response.data.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const orderSlice = createSlice({
  name: 'order',
  initialState: {
    orders: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchOrdersAsync.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchOrdersAsync.fulfilled, (state, action) => {
        state.loading = false;
        state.orders = action.payload;
      })
      .addCase(fetchOrdersAsync.rejected, (state, action) => {
        state.loading = false;
        state.error =
          action.error.message || 'An error occurred while fetching orders.';
      })
      .addCase(deleteOrderAsync.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(deleteOrderAsync.fulfilled, (state, action) => {
        state.loading = false;
        state.orders = state.orders.filter(
          (order) => order.order_id !== action.payload
        );
      })
      .addCase(deleteOrderAsync.rejected, (state, action) => {
        state.loading = false;
        state.error =
          action.error.message || 'An error occurred while deleting the order.';
      });
  },
});

export default orderSlice.reducer;
