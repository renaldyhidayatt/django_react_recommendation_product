import { SweetAlert } from '@/helpers';
import { deleteOrderAsync, fetchOrdersAsync } from '@/redux/order';
import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const OrderPage = () => {
  const dispatch = useDispatch();

  const order = useSelector((state) => state.orderReducer);

  const { error, loading, orders } = order;

  const itemsPerPage = 10;
  const [currentPage, setCurrentPage] = useState(1);
  const [filteredOrder, setFilteredOrder] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    dispatch(fetchOrdersAsync());
  }, []);

  useEffect(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    setFilteredOrder(orders.slice(startIndex, endIndex));
  }, [currentPage, orders]);

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this record?')) {
      dispatch(deleteOrderAsync(id))
        .then(() => {
          SweetAlert.success('Success', 'Item Remove Order').then(() =>
            dispatch(fetchOrdersAsync())
          );
        })
        .catch(() => {
          SweetAlert.error('Error', 'Failed to remove item from Order');
        });
    }
  };

  const handleSearch = (e) => {
    setCurrentPage(1);
    setSearchTerm(e.target.value);
  };

  const filteredData = orders.filter((order) => {
    return (
      order.id.toString().includes(searchTerm) || // Filter berdasarkan ID pesanan
      order.name.toLowerCase().includes(searchTerm.toLowerCase()) || // Filter berdasarkan nama pelanggan
      order.shipping_address.provinsi
        .toLowerCase()
        .includes(searchTerm.toLowerCase()) || // Filter berdasarkan provinsi
      order.shipping_address.kota
        .toLowerCase()
        .includes(searchTerm.toLowerCase()) || // Filter berdasarkan kota
      order.shipping_address.alamat
        .toLowerCase()
        .includes(searchTerm.toLowerCase()) || // Filter berdasarkan alamat
      order.courier.toLowerCase().includes(searchTerm.toLowerCase()) || // Filter berdasarkan kurir
      order.shippingMethod.toLowerCase().includes(searchTerm.toLowerCase()) || // Filter berdasarkan metode pengiriman
      order.shippingCost.toString().includes(searchTerm) || // Filter berdasarkan biaya pengiriman
      order.totalPrice.toString().includes(searchTerm) || // Filter berdasarkan total harga
      order.totalProduct.toString().includes(searchTerm) // Filter berdasarkan total produk
    );
  });

  const pageCount = Math.ceil(filteredData.length / itemsPerPage);
  const displayedOrders = filteredData.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );
  const currentBlock = Math.ceil(currentPage / 5);

  if (loading) {
    return <h1>Loading</h1>;
  }

  return (
    <div className="page-heading">
      <div className="page-title">
        <div className="row">
          <div className="col-12 col-md-6 order-md-1 order-last">
            <h3>order</h3>
            {error && (
              <div
                className="alert alert-danger alert-dismissible fade show"
                role="alert"
              >
                {error}
                <button
                  type="button"
                  className="btn-close"
                  data-bs-dismiss="alert"
                  aria-label="Close"
                ></button>
              </div>
            )}
          </div>
          <div className="col-12 col-md-6 order-md-2 order-first">
            <nav
              aria-label="breadcrumb"
              className="breadcrumb-header float-start float-lg-end"
            >
              <ol className="breadcrumb">
                <li className="breadcrumb-item">
                  <a href="index.html">Dashboard</a>
                </li>
                <li className="breadcrumb-item active" aria-current="page">
                  Order
                </li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
      <section className="section">
        <div className="card">
          <div className="card-header"></div>
          <div className="card-body">
            <div className="mb-3">
              <input
                type="text"
                className="form-control"
                placeholder="Search by name or description"
                value={searchTerm}
                onChange={handleSearch}
              />
            </div>
            <table className="table table-striped" id="table1">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Nama</th>
                  <th>Phone</th>
                  <th>Provinsi</th>
                  <th>Kota</th>
                  <th>Alamat</th>
                  <th>Kurir</th>
                  <th>shippingMethod</th>
                  <th>shippingCost</th>
                  <th>Total Price</th>
                  <th>Total Product</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {displayedOrders.map((row) => (
                  <tr key={row.id}>
                    <td>{row.id}</td>
                    <td>{row.name}</td>
                    <td>{row.phone}</td>
                    <td>{row.shipping_address.provinsi}</td>
                    <td>{row.shipping_address.kota}</td>
                    <td>{row.shipping_address.alamat}</td>
                    <td>{row.courier}</td>
                    <td>{row.shippingMethod}</td>
                    <td>{row.shippingCost}</td>
                    <td>{row.totalPrice}</td>
                    <td>{row.totalProduct}</td>

                    <td width="250">
                      <a
                        onClick={() => handleDelete(row.id)}
                        className="btn btn-danger"
                      >
                        Delete
                      </a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            <nav aria-label="Page navigation example">
              <ul className="pagination pagination-primary">
                <li
                  className={`page-item ${currentPage === 1 ? 'disabled' : ''}`}
                >
                  <span
                    className="page-link"
                    onClick={() => setCurrentPage(currentPage - 1)}
                  >
                    Previous
                  </span>
                </li>
                {[...Array(pageCount > 5 ? 5 : pageCount)].map((_, index) => (
                  <li key={index} className="page-item">
                    <span
                      className={`page-link ${
                        currentPage === index + 1 + (currentBlock - 1) * 5
                          ? 'active'
                          : ''
                      }`}
                      onClick={() =>
                        setCurrentPage(index + 1 + (currentBlock - 1) * 5)
                      }
                    >
                      {index + 1 + (currentBlock - 1) * 5}
                    </span>
                  </li>
                ))}
                <li
                  className={`page-item ${
                    currentPage * itemsPerPage >= filteredData.length
                      ? 'disabled'
                      : ''
                  }`}
                >
                  <span
                    className="page-link"
                    onClick={() => setCurrentPage(currentPage + 1)}
                  >
                    Next
                  </span>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </section>
    </div>
  );
};

export default OrderPage;
