'use client';

import { SweetAlert } from '@/helpers';
import { deleteSliderById, fetchAllSliders } from '@/redux/slider';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

const SliderPage = () => {
  const { sliders, error, loading } = useSelector(
    (state) => state.sliderReducer
  );

  const dispatch = useDispatch();

  const handleDeleteSlider = (id) => {
    const confirmed = window.confirm(
      'Apakah Anda yakin ingin menghapus rekaman ini?'
    );
    if (confirmed) {
      dispatch(deleteSliderById(id))
        .then(() => {
          SweetAlert.success('Success', 'Slider berhasil dihapus');

          dispatch(fetchAllSliders());
        })
        .catch(() => {
          SweetAlert.error('Error', 'Failed to remove item from Slider');
        });
    }
  };

  useEffect(() => {
    dispatch(fetchAllSliders()).then((data) => console.log(data));
  }, []);

  if (loading) {
    return <h1>Loading</h1>;
  }

  return (
    <div className="page-heading">
      <div className="page-title">
        <div className="row">
          <div className="col-12 col-md-6 order-md-1 order-last">
            <h3>Slider - Page</h3>
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
                  <Link href={'/admin'}>Dashboard</Link>
                </li>
                <li className="breadcrumb-item active" aria-current="page">
                  Slider
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
              data-bs-target="#slider"
            >
              <i className="fas fa-user"></i> Add Slider
            </button>
          </div>
          <div className="card-body">
            <table className="table table-striped" id="table1">
              <thead>
                <tr>
                  <th>No</th>
                  <th>Nama</th>
                  <th>Image</th>
                  <th>Created_at</th>
                  <th>Updated_at</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {sliders &&
                  sliders.map((row) => (
                    <tr key={row.id}>
                      <td>{row.id}</td>
                      <td>{row.name}</td>
                      <td>
                        <img
                          src={row.image}
                          alt="Current Image"
                          width={100}
                          height={100}
                        />
                      </td>
                      <td>{row.created_at}</td>
                      <td>{row.updated_at}</td>
                      <td width="250">
                        <Link
                          to={`/admin/slider/edit/${row.id}`}
                          className="btn btn-success"
                        >
                          Edit
                        </Link>
                        <button
                          onClick={() => handleDeleteSlider(row.id)}
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

export default SliderPage;
