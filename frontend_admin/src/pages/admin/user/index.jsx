import { SweetAlert } from '@/helpers';
import { deleteUserById, fetchUsers } from '@/redux/user';
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

const UserPage = () => {
  const myuser = useSelector((state) => state.userReducer);

  const { users, loading, error } = myuser;

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUsers())
      .then((data) => console.log(data))
      .catch((error) => {
        console.log(error);
      });
  }, [dispatch]);

  const handleDeleteUser = (userId) => {
    dispatch(deleteUserById(id))
      .then(() => {
        SweetAlert.success('Success', 'Item Remove Category');
      })
      .catch(() => {
        SweetAlert.error('Error', 'Failed to remove item from Category');
      });
  };

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
              data-bs-target="#user"
            >
              <i className="fas fa-user" /> Add User
            </button>
          </div>
          <div className="card-body">
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
                {users.map((user) => (
                  <tr key={user.id}>
                    <td>{user.id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.created_at}</td>
                    <td>{user.updated_at}</td>
                    <td width={250}>
                      <a
                        href={`/admin/user/edit/${user.id}`}
                        className="btn btn-success"
                      >
                        Edit
                      </a>
                      <button
                        onClick={() => handleDeleteUser(user.id)}
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

export default UserPage;
