import { fetchAllCategories } from '@/redux/category';
import { fetchProductById, updateProductById } from '@/redux/product';

import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate, useParams } from 'react-router-dom';

const EditProductPage = () => {
  const { id } = useParams();
  const categoryState = useSelector((state) => state.categoryReducer);
  const productState = useSelector((state) => state.productReducer);

  const { product, loading, error } = productState;

  const [formData, setFormData] = useState({
    name: '',
    image: null,
    categoryId: '',
    description: '',
    price: '',
    brand: '',
    weight: '',
    rating: '',
    countInStock: '',
  });

  const handleNameChange = (e) => {
    setFormData({
      ...formData,
      name: e.target.value,
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

  const handleCategoryIdChange = (e) => {
    setFormData({
      ...formData,
      categoryId: e.target.value,
    });
  };

  const handleDescriptionChange = (e) => {
    setFormData({
      ...formData,
      description: e.target.value,
    });
  };

  const handlePriceChange = (e) => {
    setFormData({
      ...formData,
      price: e.target.value,
    });
  };

  const handleBrandChange = (e) => {
    setFormData({
      ...formData,
      brand: e.target.value,
    });
  };

  const handleWeightChange = (e) => {
    setFormData({
      ...formData,
      weight: e.target.value,
    });
  };

  const handleRatingChange = (e) => {
    setFormData({
      ...formData,
      rating: e.target.value,
    });
  };

  const handleCountInStockChange = (e) => {
    setFormData({
      ...formData,
      countInStock: e.target.value,
    });
  };

  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = new FormData();

    form.append('name', formData.name);
    form.append('category', formData.categoryId);
    form.append('description', formData.description);
    form.append('countInStock', formData.countInStock);
    form.append('brand', formData.brand);
    form.append('weight', formData.weight);
    form.append('rating', formData.rating);
    form.append('price', formData.price);
    if (formData.image) {
      form.append('image_product', formData.image);
    }

    dispatch(updateProductById({ id, form })).then((data) => {
      console.log('update: ', data);
      navigate('/admin/product');
    });
  };

  useEffect(() => {
    if (id) {
      dispatch(fetchProductById(id)).then((data) => {
        console.log(data);
      });
      dispatch(fetchAllCategories()).then((data) => {
        console.log('Category:', data);
      });
    }
  }, []);

  useEffect(() => {
    if (product) {
      setFormData({
        ...formData,
        name: product.name,
        price: product.price.toString(),
        categoryId: product.category,
        description: product.description,
        brand: product.brand,
        weight: product.weight,
        rating: product.rating,
        countInStock: product.countInStock.toString(),
      });
    }
  }, [product]);

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
            <h3>Edit Product</h3>
          </div>
          <div className="card-body">
            {loading ? (
              <h1>Loading</h1>
            ) : (
              <form onSubmit={handleSubmit}>
                <label htmlFor="name_produk">Nama Produk: </label>
                <div className="form-group">
                  <input
                    id="name_produk"
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleNameChange}
                    placeholder="Nama Produk"
                    className="form-control"
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="image" className="form-label">
                    Gambar
                  </label>
                  <input
                    type="file"
                    name="image"
                    onChange={handleImageChange}
                    className="form-control"
                    id="image"
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="current_image" className="form-label">
                    Gambar Saat Ini
                  </label>
                  <br />
                  {product?.image_product ? (
                    <img
                      src={product.image_product}
                      alt="Current Image"
                      width={100}
                      height={100}
                    />
                  ) : (
                    <span>Tidak ada gambar</span>
                  )}
                </div>
                <label htmlFor="category_id">ID Kategori: </label>
                <div className="form-group">
                  <select
                    name="category_id"
                    value={formData.categoryId || product?.categoryId}
                    onChange={handleCategoryIdChange}
                    className="form-control"
                  >
                    <option value="">Pilih Kategori</option>
                    {categoryState &&
                      categoryState.categories.map((k) => (
                        <option key={k.id} value={k.id}>
                          {k.name}
                        </option>
                      ))}
                  </select>
                </div>
                <label htmlFor="description">Deskripsi: </label>
                <div className="form-group">
                  <textarea
                    id="description"
                    name="description"
                    placeholder="Deskripsi"
                    className="form-control"
                    value={formData.description}
                    onChange={handleDescriptionChange}
                  />
                </div>

                <label htmlFor="brand">Brand: </label>
                <div className="form-group">
                  <input
                    type="text"
                    placeholder="Brand"
                    className="form-control"
                    id="brand"
                    name="brand"
                    value={formData.brand}
                    onChange={handleBrandChange}
                  />
                </div>
                <label htmlFor="weight">Weight: </label>
                <div className="form-group">
                  <input
                    type="text"
                    placeholder="Weight"
                    className="form-control"
                    id="weight"
                    name="weight"
                    value={formData.weight}
                    onChange={handleWeightChange}
                  />
                </div>

                <label htmlFor="rating">Rating: </label>
                <div className="form-group">
                  <input
                    type="text"
                    placeholder="Rating"
                    className="form-control"
                    id="rating"
                    value={formData.rating}
                    name="rating"
                    onChange={handleRatingChange}
                  />
                </div>

                <label htmlFor="price">Harga: </label>
                <div className="form-group">
                  <input
                    id="price"
                    type="text"
                    name="price"
                    placeholder="Harga"
                    className="form-control"
                    value={formData.price}
                    onChange={handlePriceChange}
                  />
                </div>
                <label htmlFor="countInStock">Jumlah Stok: </label>
                <div className="form-group">
                  <input
                    id="countInStock"
                    type="text"
                    name="countInStock"
                    placeholder="Jumlah Stok"
                    className="form-control"
                    value={formData.countInStock}
                    onChange={handleCountInStockChange}
                  />
                </div>

                <button type="submit" name="submit" className="btn btn-primary">
                  Submit
                </button>
              </form>
            )}
          </div>
        </div>
      </section>
    </div>
  );
};

export default EditProductPage;
