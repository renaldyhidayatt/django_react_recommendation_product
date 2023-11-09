import { configureStore } from '@reduxjs/toolkit';
import { registerSlice, loginSlice } from './auth.slice';
import { updateSlice, getAllUsersSlice, deleteUserSlice } from './user.slice';
import sliderSlice from './slider.slice';
import categorySlice from './category.slice';
import productSlice from './product.slice';
import cartSlice from './cart.slice';
import orderSlice from './order.slice';
import reviewSlice from './review.slice';
import rajaongkirSlice from './rajaongkir.slice';

const store = configureStore({
  reducer: {
    updateUserReducer: updateSlice.reducer,
    getAllUsersReducer: getAllUsersSlice.reducer,
    deleteUserReducer: deleteUserSlice.reducer,
    loginReducer: loginSlice.reducer,
    registerReducer: registerSlice.reducer,
    sliderReducer: sliderSlice,
    categoryReducer: categorySlice,
    productReducer: productSlice,
    cartReducer: cartSlice,
    orderReducer: orderSlice,
    reviewReducer: reviewSlice,
    rajaongkirReducer: rajaongkirSlice,
  },
});

export default store;
