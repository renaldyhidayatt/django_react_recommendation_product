import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';

export const fetchProducts = createAsyncThunk(
  'products/fetchProducts',
  async (_, { rejectWithValue }) => {
    try {
      const response = await myApi.get('/product/recom');
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const fetchProductById = createAsyncThunk(
  'products/fetchProductById',
  async (id, { rejectWithValue }) => {
    try {
      const response = await myApi.get(`/product/${id}`);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const fetchProductBySlug = createAsyncThunk(
  'products/fetchProductBySlug',
  async (slug, { rejectWithValue }) => {
    try {
      const response = await myApi.get(`/product/slug/${slug}`);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const addProductReview = createAsyncThunk(
  'product/addProductReview',
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

export const createProduct = createAsyncThunk(
  'products/createProduct',
  async (productData, { rejectWithValue, getState }) => {
    try {
      const token = getState().auth.token;
      const response = await myApi.post(`/product/create`, productData, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const updateProductById = createAsyncThunk(
  'products/updateProductById',
  async ({ id, form }, { rejectWithValue, getState }) => {
    try {
      const token = getState().auth.token;
      const response = await myApi.put(`/product/${id}`, form, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const deleteProductById = createAsyncThunk(
  'products/deleteProductById',
  async (id, { rejectWithValue, getState }) => {
    try {
      const token = getState().auth.token;
      await myApi.delete(`/product/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return 
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const updateQuantity = createAsyncThunk(
  'products/updateQuantity',
  async (cart, { rejectWithValue, getState }) => {
    try {
      const token = getState().auth.token;
      const response = await myApi.post(
        '/product/updatequantity',
        {
          cart: cart,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const initialState = {
  product: null,
  products: [],
  selectedProduct: null,
  loading: false,
  error: null,
};

const productSlice = createSlice({
  name: 'products',
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchProducts.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProducts.fulfilled, (state, action) => {
        state.loading = false;
        state.products = action.payload;
      })
      .addCase(fetchProducts.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })
      .addCase(fetchProductById.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProductById.fulfilled, (state, action) => {
        state.loading = false;
        state.product = action.payload;
      })
      .addCase(fetchProductById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })
      .addCase(fetchProductBySlug.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProductBySlug.fulfilled, (state, action) => {
        state.loading = false;
        state.product = action.payload;
      })
      .addCase(fetchProductBySlug.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })

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
      })
      .addCase(createProduct.fulfilled, (state, action) => {
        state.products.push(action.payload);
      })
      .addCase(updateProductById.fulfilled, (state, action) => {
        const index = state.products.findIndex(
          (product) => product.product_id === action.payload.id
        );
        if (index !== -1) {
          state.products[index] = action.payload;
        }
        state.selectedProduct = action.payload;
      })
      .addCase(deleteProductById.fulfilled, (state, action) => {
        state.products = state.products.filter(
          (product) => product.product_id !== action.payload
        );
        state.selectedProduct = null;
      })
      .addCase(updateQuantity.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(updateQuantity.fulfilled, (state, action) => {
        state.loading = false;
        state.selectedProduct = action.payload;
      })
      .addCase(updateQuantity.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export default productSlice.reducer;
