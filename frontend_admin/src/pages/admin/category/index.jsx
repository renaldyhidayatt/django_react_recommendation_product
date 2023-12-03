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
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    dispatch(fetchAllCategories());
  }, []);

  useEffect(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    setFilteredCategories(categories.slice(startIndex, endIndex));
  }, [currentPage, categories]);

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this record?')) {
      dispatch(deleteCategoryById(id))
        .then(() => {
          SweetAlert.success('Success', 'Item Remove Category').then(() =>
            dispatch(fetchAllCategories())
          );
        })

        .catch(() => {
          SweetAlert.error('Error', 'Failed to remove item from Category');
        });
    }
  };

  const handleSearch = (e) => {
    setCurrentPage(1);
    setSearchTerm(e.target.value);
  };

  const filteredData = categories.filter((category) => {
    return (
      category.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      category.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
  });

  const pageCount = Math.ceil(filteredData.length / itemsPerPage);
  const displayedCategories = filteredData.slice(
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
            <h3>Category</h3>
            {error && (
              <div
                className="alert alert-danger alert-dismissible fade show"
                role="alert"
              >
                {error.message}
                <button
                  type="button"
                  className="btn-close"
                  data-bs-dismiss="alert"
                  aria-label="Close"
                />
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
                <li className="breadcrumb-item active" aria-current="page"></li>
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
                  <th>Nama Kategori</th>
                  <th>Description</th>
                  <th>Image</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {displayedCategories.map((row, index) => (
                  <tr key={row.id}>
                    <td>{(currentPage - 1) * itemsPerPage + index + 1}</td>
                    <td>{row.name}</td>
                    <td>{row.description}</td>
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

export default CategoryPage;
