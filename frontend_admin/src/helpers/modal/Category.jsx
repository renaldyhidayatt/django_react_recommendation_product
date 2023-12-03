import { createCategory } from '@/redux/category';
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import SweetAlert from '../sweetalert';
import { fetchAllCategories } from '@/redux/category'

function ModalCategory() {
  const [formData, setFormData] = useState({
    name: '',
    description: "",
    image: null,
  });

  const dispatch = useDispatch();

  const handleNameChange = (e) => {
    setFormData({
      ...formData,
      name: e.target.value,
    });
  };

  const handleDescriptionChange = (e) => {
    setFormData({
      ...formData,
      description: e.target.value,
    });
  };

  const handleImageChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setFormData({
        ...formData,
        image: e.target.files[0],
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const form = new FormData();
    form.append('name', formData.name);
    form.append("description", formData.description)
    if (formData.image) {
      form.append('image_category', formData.image);
    }

    dispatch(createCategory(form)).then(() => {
      SweetAlert.success("Successfully", "Category created successfully").then(() => dispatch(fetchAllCategories()));
    }).catch(() => {
      SweetAlert.error("Error!!!",  "Failed to create Category. Please try again.")
    })
  };

  return (
    <div
      className="modal fade text-left"
      id="category"
      tabIndex={-1}
      role="dialog"
      aria-labelledby="category"
      aria-hidden="true"
    >
      <div
        className="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-lg"
        role="document"
      >
        <div className="modal-content">
          <div className="modal-header">
            <h4 className="modal-title" id="category">
              Add Kategori
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
              <label htmlFor="name_kategori">Nama Kategori: </label>
              <div className="form-group">
                <input
                  id="name_kategori"
                  type="text"
                  name="nama_kategori"
                  placeholder="Nama Kategori"
                  className="form-control"
                  value={formData.name}
                  onChange={handleNameChange}
                />
              </div>
              <label htmlFor="description">Description: </label>
              <div className="form-group">
                <input
                  id="description"
                  type="text"
                  name="description"
                  placeholder="Description"
                  className="form-control"
                  value={formData.description}
                  onChange={handleDescriptionChange}
                />
              </div>
              <label htmlFor="image">image: </label>
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
                <i className="bx bx-x d-block d-sm-none" />
                <span className="d-none d-sm-block">Close</span>
              </button>
              <button
                type="submit"
                className="btn btn-primary ms-1"
                data-bs-dismiss="modal"
              >
                <i className="bx bx-check d-block d-sm-none" />
                <span className="d-none d-sm-block">Adding</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default ModalCategory;
