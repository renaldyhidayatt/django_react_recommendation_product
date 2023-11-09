import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { deleteCategoryById, fetchAllCategories } from '@/redux/category';
import { SweetAlert } from '@/helpers';
import { Link } from 'react-router-dom';

const CategoryPage = () => {
  const category = useSelector((state) => state.categoryReducer);
  const { error, loading, categories } = category;
  const dispatch = useDispatch();

  const itemsPerPage = 10;
  const [currentPage, setCurrentPage] = useState(1);
  const [filteredCategories, setFilteredCategories] = useState([]);

  useEffect(() => {
    dispatch(fetchAllCategories());
  }, []);

  useEffect(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    setFilteredCategories(categories.slice(startIndex, endIndex));
  }, [currentPage, categories]);

  const handleDelete = (id) => {
    dispatch(deleteCategoryById(id))
      .then(() => {
        SweetAlert.success('Success', 'Item Remove Category');
      })
      .catch(() => {
        SweetAlert.error('Error', 'Failed to remove item from Category');
      });
  };

  if (loading) {
    return <h1>Loading</h1>;
  }

  return (
    <div className="page-heading">
      <div className="page-title">
        <div className="row">
          <div className="col-12 col-md-6 order-md-1 order-last">
            <h3>category</h3>
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
                  Category
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
              data-bs-target="#category"
            >
              <i className="fas fa-user"></i> Add Category
            </button>
          </div>
          <div className="card-body">
            <table className="table table-striped" id="table1">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Nama Kategori</th>
                  <th>Image</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {filteredCategories.map((row, index) => (
                  <tr key={row.id}>
                    <td>{(currentPage - 1) * itemsPerPage + index + 1}</td>
                    <td>{row.name}</td>
                    <td>
                      <img
                        src={row.image_category}
                        alt="Current Image"
                        width={100}
                        height={100}
                      />
                    </td>
                    <td width="250">
                      <Link
                        to={`/admin/category/edit/${row.id}`}
                        className="btn btn-success"
                      >
                        Edit
                      </Link>
                      <button
                        onClick={() => handleDelete(row.id)}
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
                    currentPage * itemsPerPage >= categories.length
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

export default CategoryPage;
