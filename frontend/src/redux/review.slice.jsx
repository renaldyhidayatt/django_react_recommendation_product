import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';

export const addProductReview = createAsyncThunk(
  'review/addProductReview',
  async ({ review, productid }, { rejectWithValue, getState }) => {
    try {
      const accessToken = getState().loginReducer.accessToken;

      if (!accessToken) {
        console.error('accessToken is null');
        return rejectWithValue('accessToken is null');
      }

      const data = {
        rating: review.rating,
        comment: review.comment,
      };

      const headers = {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + accessToken,
      };

      const response = await myApi.post(`/review/create/${productid}`, data, {
        headers,
      });

      if (response.status !== 200) {
        throw new Error('Error');
      }

      return;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const reviewSlice = createSlice({
  name: 'review',
  initialState: {
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(addProductReview.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(addProductReview.fulfilled, (state) => {
        state.loading = false;
      })
      .addCase(addProductReview.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default reviewSlice.reducer;
