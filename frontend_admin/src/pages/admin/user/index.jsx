import { SweetAlert } from '@/helpers';
import { deleteUserById, fetchUsers } from '@/redux/user';
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

const UserPage = () => {
  const myuser = useSelector((state) => state.userReducer);

  const { users, loading, error } = myuser;

  const itemsPerPage = 10;
  const [currentPage, setCurrentPage] = useState(1);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUsers())
      .then((data) => console.log(data))
      .catch((error) => {
        console.log(error);
      });
  }, [dispatch]);

  useEffect(() => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    setFilteredUsers(users.slice(startIndex, endIndex));
  }, [currentPage, users]);

  const handleDeleteUser = (userId) => {
    if (window.confirm('Are you sure you want to delete this record?')) {
      dispatch(deleteUserById(userId))
        .then(() => {
          SweetAlert.success('Success', 'Item Remove User').then(() => {
            dispatch(fetchUsers());
          });
        })
        .catch(() => {
          SweetAlert.error('Error', 'Failed to remove item from User');
        });
    }
  };

  const handleSearch = (e) => {
    setCurrentPage(1);
    setSearchTerm(e.target.value);
  };

  const filteredData = users.filter((user) => {
    return (
      user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase())
    );
  });

  const pageCount = Math.ceil(filteredData.length / itemsPerPage);
  const displayedUsers = filteredData.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );

  const currentBlock = Math.ceil(currentPage / 5);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="page-heading">
      <div className="page-title">
        <div className="row">
          <div className="col-12 col-md-6 order-md-1 order-last">
            <h3>User</h3>
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
                  <Link to="/admin/dashboard">Dashboard</Link>
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
              data-bs-target="#user"
            >
              <i className="fas fa-user" /> Add User
            </button>
          </div>
          <div className="card-body">
            <div className="mb-3">
              <input
                type="text"
                className="form-control"
                placeholder="Search by name or email"
                value={searchTerm}
                onChange={handleSearch}
              />
            </div>
            <table className="table table-striped" id="table1">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Created_at</th>
                  <th>Updated_at</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {displayedUsers.map((row, index) => (
                  <tr key={row.id}>
                    <td>{(currentPage - 1) * itemsPerPage + index + 1}</td>
                    <td>{row.name}</td>
                    <td>{row.email}</td>
                    <td>{row.created_at}</td>
                    <td>{row.updated_at}</td>
                    <td width={250}>
                      <Link
                        to={`/admin/user/edit/${row.id}`}
                        className="btn btn-success"
                      >
                        Edit
                      </Link>
                      <button
                        onClick={() => handleDeleteUser(row.id)}
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

export default UserPage;
