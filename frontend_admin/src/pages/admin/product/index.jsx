import { SweetAlert } from '@/helpers';
import { deleteProduct, fetchAllProducts } from '@/redux/product';
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

const ProductPage = () => {
  const product = useSelector((state) => state.productReducer);

  const dispatch = useDispatch();
  const { products, loading, error } = product;

  const itemsPerPage = 10;
  const [currentPage, setCurrentPage] = useState(1);
  const [filteredProducts, setFilteredProducts] = useState([]);

  useEffect(() => {
    dispatch(fetchAllProducts());
  }, []);

  useEffect(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    setFilteredProducts(products.slice(startIndex, endIndex));
  }, [currentPage, products]);

  const handleDeleteProduct = (id) => {
    dispatch(deleteProduct(id))
      .then(() => {
        SweetAlert.success('Success', 'Produk berhasil dihapus');

        dispatch(fetchAllProducts());
      })
      .catch(() => {
        SweetAlert.error('Error', 'Failed to remove item from Category');
      });
  };

  return (
    <div className="page-heading">
      <div className="page-title">
        <div className="row">
          <div className="col-12 col-md-6 order-md-1 order-last">
            <h3>Product</h3>
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
                  product
                </li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
      <section className="section">
        <div className="card">
          <div className="card-header">
            <button
              type="button"
              className="btn btn-primary btn-sm mb-3"
              data-bs-toggle="modal"
              data-bs-target="#product"
            >
              <i className="fas fa-user"></i> Add Product
            </button>
          </div>
          <div className="card-body">
            <table className="table table-striped" id="table1">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Nama</th>
                  <th>Brand</th>
                  <th>Image</th>
                  <th>Category_id</th>
                  <th>Description</th>
                  <th>Price</th>
                  <th>CountInStock</th>
                  <th>Created_at</th>
                  <th>Updated_at</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {filteredProducts.map((row, index) => (
                  <tr key={row.id}>
                    <td>{(currentPage - 1) * itemsPerPage + index + 1}</td>
                    <td>{row.name}</td>
                    <td>{row.brand}</td>
                    <td>
                      <img
                        src={row.image_product}
                        alt="Current Image"
                        width={100}
                        height={100}
                      />
                    </td>
                    <td>{row.category}</td>
                    <td>{row.description}</td>

                    <td>{row.price}</td>
                    <td>{row.countInStock}</td>
                    <td>{row.created_at}</td>
                    <td>{row.updated_at}</td>
                    <td width="250">
                      <Link
                        to={`/admin/product/edit/${row.id}`}
                        className="btn btn-success"
                      >
                        Edit
                      </Link>
                      <button
                        onClick={() => handleDeleteProduct(row.id)}
                        className="btn btn-danger"
                      >
                        Delete
                      </button>
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
                <li className="page-item">
                  <span className="page-link active">Page {currentPage}</span>
                </li>
                <li
                  className={`page-item ${
                    currentPage * itemsPerPage >= products.length
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

export default ProductPage;
