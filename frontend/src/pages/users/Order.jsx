import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getOrdersByUserId } from '../../redux/order.slice';
import { Navigate } from 'react-router-dom';
import { LoadingIndicator } from '../../components/Loading';
import { IsError } from '../../components/ISError';

export default function OrderPage() {
  const orderState = useSelector((state) => state.orderReducer);
  const user = useSelector((state) => state.authReducer.user);

  const { orders, getOrdersByUserIdError, getOrdersByUserIdLoading } =
    orderState;

  const dispatch = useDispatch();

  useEffect(() => {
    if (user) {
      dispatch(getOrdersByUserId());
    } else {
      <Navigate to="/login" />;
    }
  }, [dispatch]);

  return (
    <div>
      <div className="flex justify-center mt-5">
        <div className="w-3/4">
          <h2 className="text-2xl font-semibold">MY ORDERS</h2>
          <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead>
              <tr>
                <th>Order ID</th>
                <th>Amount</th>
                <th>Date</th>
                <th>Transaction ID</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {getOrdersByUserIdLoading && <LoadingIndicator />}
              {orders &&
                orders.map((order) => {
                  return (
                    <tr
                      key={order.id}
                      onClick={() => {
                        window.location = `/user/orderinfo/${order.id}`;
                      }}
                    >
                      <td>{order.id}</td>
                      <td>{order.orderAmount}</td>
                      <td>{order.created_at.substring(0, 10)}</td>
                      <td>{order.transactionId}</td>
                      <td>
                        {order.isDelivered ? (
                          <li>Delivered</li>
                        ) : (
                          <li>Order Placed</li>
                        )}
                      </td>
                    </tr>
                  );
                })}
              {getOrdersByUserIdError && (
                <IsError error="something went wrong" />
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
