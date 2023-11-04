export const calculateSubtotal = (cartItems) => {
    return cartItems.reduce((total, item) => {
        return total + item.quantity * item.price;
    }, 0);
};

export const calculateTotalProducts = (cartItems) => {
    return cartItems.reduce((total, item) => {
        return total + item.quantity;
    }, 0);
};

export const calculateWeight = (cartItems) => {
    return cartItems.reduce((totalWeight, item) => {
        return totalWeight + item.quantity * item.weight;
    }, 0);
};