import { useParams } from 'react-router-dom';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { LoadingIndicator } from '../../components/Loading';
import { IsError } from '../../components/ISError';
import { getOrderById } from '../../redux/order.slice';

export default function OrderInfo() {
    const { id } = useParams();
    const dispatch = useDispatch();
    const orderState = useSelector((state) => state.orderReducer);
    const { order, getOrderByIdLoading, getOrderByIdError } = orderState;

    useEffect(() => {
        dispatch(getOrderById(id));
    }, [dispatch, id]);

    return (
        <div className="flex justify-center items-center min-h-screen mt-100">
            <div className="bg-white w-full md:w-2/3 p-4 rounded-lg shadow-lg">
                {getOrderByIdError && <IsError error={getOrderByIdError} />}
                {getOrderByIdLoading ? (
                    <LoadingIndicator />
                ) : (
                    order && (
                        <div className="grid grid-cols-2 gap-4 mt-10">
                            <div className="bg-white rounded-lg p-4">
                                <h2 className="text-xl font-semibold">Items In Your Order</h2>
                                <hr className="my-2" />
                                {order.order_items.map((item) => (
                                    <div className="orderitem" key={item.id}>
                                        <h1>{item.name}</h1>
                                        <h1>
                                            Quantity: <b>{item.quantity}</b>
                                        </h1>
                                        <h1>
                                            Price: {item.price} * {item.quantity} ={' '}
                                            {item.price * item.quantity}
                                        </h1>
                                        <hr className="my-2" />
                                    </div>
                                ))}
                            </div>
                            <div className="bg-white rounded-lg p-4">
                                <h2 className="text-xl font-semibold">Order Details</h2>
                                <hr className="my-2" />
                                <h3>Order Id: {order.id}</h3>
                                <h3>Total Amount: {order.totalPrice}</h3>
                                <h3>Date Of order: {order.created_at.substring(0, 10)}</h3>
                                <h3>Transaction ID: {order.transactionId}</h3>
                                {order.isDelivered ? (
                                    <h3>Order Delivered</h3>
                                ) : (
                                    <h3>Order Placed</h3>
                                )}
                                <hr className="my-2" />
                                <div className="text-right">
                                    <h2 className="text-xl font-semibold">Shipping Details</h2>
                                    <hr className="my-2" />
                                    <h1 className="text-right">
                                        Address: <b>{order.shipping_address.alamat}</b>
                                    </h1>
                                    <h1 className="text-right">
                                        City: <b>{order.shipping_address.kota}</b>
                                    </h1>
                                    <h1 className="text-right">
                                        Country: <b>{order.shipping_address.negara}</b>
                                    </h1>
                                </div>
                            </div>
                        </div>
                    )
                )}
                <hr className="my-4" />
                <div className="text-center">
                    <h2 className="text-xl font-semibold">Replacement Conditions</h2>
                    <p className="text-left">
                        A free replacement cannot be created for an item which was returned
                        and replaced once earlier. If your item is not eligible for free
                        replacement due to any reason, you can always return it for a
                        refund. If the item has missing parts or accessories, you may try to
                        contact the manufacturer for assistance. Manufacturer contact
                        information can usually be found on the item packaging or in the
                        paperwork included with the item.
                    </p>
                </div>
            </div>
        </div>
    );
}
