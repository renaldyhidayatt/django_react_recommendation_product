import { createSlider } from '@/redux/slider';
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

export default function ModalSlider(props) {
  const [nama, setNama] = useState('');
  const [image, setImage] = useState('');
  const dispatch = useDispatch();

  const handleNamaChange = (e) => {
    setNama(e.target.value);
  };

  const handleImageChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setImage(e.target.files[0]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();

    formData.append('name', nama);
    if (image) {
      formData.append('image', image);
    }

    dispatch(createSlider(formData));
  };

  return (
    <div
      className="modal fade text-left"
      id="slider"
      tabIndex={-1}
      role="dialog"
      aria-labelledby="slider"
      aria-hidden="true"
    >
      <div
        className="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-lg"
        role="document"
      >
        <div className="modal-content">
          <div className="modal-header">
            <h4 className="modal-title" id="slider">
              Add Slider
            </h4>
            <button
              type="button"
              className="close"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              <i data-feather="x" />
            </button>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="modal-body">
              <label htmlFor="nama">Nama: </label>
              <div className="form-group">
                <input
                  id="nama"
                  type="text"
                  name="nama"
                  placeholder="Nama"
                  className="form-control"
                  value={nama}
                  onChange={handleNamaChange}
                />
              </div>
              <label htmlFor="image">Image: </label>
              <div className="form-group">
                <input
                  type="file"
                  className="form-control"
                  id="image"
                  name="image"
                  onChange={handleImageChange}
                />
              </div>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-light-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button
                type="submit"
                className="btn btn-primary ms-1"
                data-bs-dismiss="modal"
              >
                Adding
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
