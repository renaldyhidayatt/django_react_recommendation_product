import { deleteProductById, fetchAllProducts } from '@/redux/product';
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const ProductPage = () => {
  const product = useSelector((state) => state.productReducer);

  const dispatch = useDispatch();
  const { products, loading, error } = product;

  useEffect(() => {
    dispatch(fetchAllProducts());
  }, []);

  const handleDeleteProduct = (id) => {
    if (window.confirm('Are you sure you want to delete this record?')) {
      dispatch(deleteProductById(id));
    }
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
                {products &&
                  products.map((row) => (
                    <tr key={row.id}>
                      <td>{row.id}</td>
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
                        <a
                          href={`/admin/product/edit/${row.id}`}
                          className="btn btn-success"
                        >
                          Edit
                        </a>
                        <button
                          onClick={() => {
                            handleDeleteProduct(row.id);
                          }}
                          className="btn btn-danger"
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ProductPage;
