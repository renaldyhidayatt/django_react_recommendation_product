export const getCartItemById = (cartItems, cartId) => {
    return cartItems.find((item) => item.cart_id === cartId) || null;
};