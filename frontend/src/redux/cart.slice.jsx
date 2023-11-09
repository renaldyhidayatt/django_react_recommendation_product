import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { myApi } from '../helpers/api';

export const fetchCartItems = createAsyncThunk(
    'cart/fetchCartItems',
    async (_, { rejectWithValue, getState }) => {
        try {
            const accessToken = getState().loginReducer.accessToken;


            if (!accessToken) {

                console.error('accessToken is null');
                return rejectWithValue('accessToken is null');
            }

            const response = await myApi.get('/cart/user', {
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            });
            console.log(response.data);
            return response.data;
        } catch (error) {
            return rejectWithValue(error.response.data);
        }
    }
);


export const addToCart = createAsyncThunk(
    'cart/addToCart',
    async (cartDto, { rejectWithValue, getState }) => {
        try {
            const authTokens = getState().loginReducer.accessToken;

            const response = await myApi.post('/cart/create', cartDto, {
                headers: {
                    Authorization: `Bearer ${authTokens}`,
                },
            });
            return response.data;
        } catch (error) {
            console.log(error);
            return rejectWithValue(error.response.data);
        }
    }
);

export const removeFromCart = createAsyncThunk(
    'cart/removeFromCart',
    async (cartId, { rejectWithValue, getState }) => {
        try {
            const accessToken = getState().loginReducer.accessToken;


            if (!accessToken) {

                console.error('accessToken is null');
                return rejectWithValue('accessToken is null');
            }

            await myApi.delete(`/cart/delete/${cartId}`, {
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            });
            return cartId;
        } catch (error) {
            return rejectWithValue(error.response.data);
        }
    }
);

export const deleteManyFromCart = createAsyncThunk(
    'cart/deleteManyFromCart',
    async (cartIds, { rejectWithValue, getState }) => {
        try {
            const accessToken = getState().loginReducer.accessToken;


            if (!accessToken) {

                console.error('accessToken is null');
                return rejectWithValue('accessToken is null');
            }

            const response = await myApi.post(
                '/cart/delete-many',
                { cartIds: cartIds },
                {
                    headers: {
                        Authorization: `Bearer ${authTokens}`,
                    },
                }
            );
            return response.data
        } catch (error) {
            return rejectWithValue(error.response.data);
        }
    }
);

const cartSlice = createSlice({
    name: 'cart',
    initialState: {
        cartItems: [],
        loading: false,
        error: null,
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchCartItems.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(fetchCartItems.fulfilled, (state, action) => {
                state.loading = false;
                state.cartItems = action.payload;
            })
            .addCase(fetchCartItems.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            })
            .addCase(addToCart.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(addToCart.fulfilled, (state, action) => {
                state.loading = false;
                state.cartItems.push(action.payload);
            })
            .addCase(addToCart.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            })
            .addCase(removeFromCart.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(removeFromCart.fulfilled, (state, action) => {
                state.loading = false;
                const cartId = action.payload;
                state.cartItems = state.cartItems.filter(
                    (item) => item.cart_id !== cartId
                );
            })
            .addCase(removeFromCart.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            })
            .addCase(deleteManyFromCart.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(deleteManyFromCart.fulfilled, (state, action) => {
                state.loading = false;
                const deletedIds = action.payload;
                state.cartItems = state.cartItems.filter(
                    (item) => !deletedIds.includes(item.cart_id)
                );
            })
            .addCase(deleteManyFromCart.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            });
    },
});

export default cartSlice.reducer;