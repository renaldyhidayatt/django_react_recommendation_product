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

  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [countInStock, setCountInStock] = useState('');
  const [file, setFile] = useState(null);

  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();

    formData.append('name', name);
    formData.append('category', category);
    formData.append('description', description);
    formData.append('price', price);
    formData.append('countInStock', countInStock);
    if (file) {
      formData.append('image_product', file);
    }

    dispatch(updateProductById({ id, formData })).then((data) => {
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
      setName(product.name);
      setPrice(product.price.toString());
      setDescription(product.description);
      setCountInStock(product.countInStock.toString());
    }
    console.log(product);
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
                    value={name}
                    onChange={(e) => setName(e.target.value)}
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
                    onChange={(e) => {
                      const selectedFile = e.target.files?.[0];
                      setFile(selectedFile || null);
                    }}
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
                    <Image
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
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
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
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                  />
                </div>

                <label htmlFor="price">Harga: </label>
                <div className="form-group">
                  <input
                    id="price"
                    type="text"
                    name="price"
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                    placeholder="Harga"
                    className="form-control"
                  />
                </div>
                <label htmlFor="countInStock">Jumlah Stok: </label>
                <div className="form-group">
                  <input
                    id="countInStock"
                    type="text"
                    name="countInStock"
                    onChange={(e) => setCountInStock(e.target.value)}
                    value={countInStock}
                    placeholder="Jumlah Stok"
                    className="form-control"
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
