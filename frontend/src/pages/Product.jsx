import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import Review from '../components/Review';
import { addToCart } from '../redux/cart.slice';
import { fetchProductBySlug } from '../redux/product.slice';
import { LoadingIndicator } from '../components/Loading';
import { IsError } from '../components/ISError';
import SweetAlert from '../components/Sweetalert';

export default function ProductPage() {
  const { slug } = useParams();
  const dispatch = useDispatch();
  const [cartError, setCartError] = useState('');

  const user = useSelector((state) => state.loginReducer.user);

  const product = useSelector((state) => state.productReducer.product);
  const loading = useSelector((state) => state.productReducer.loading);
  const error = useSelector((state) => state.productReducer.error);

  const [quantity, setQuantity] = useState(1);

  const addCart = () => {
    if (user) {
      const parsedQuantity = parseInt(quantity);
      if (
        isNaN(parsedQuantity) ||
        parsedQuantity <= 0 ||
        parsedQuantity > product?.countInStock
      ) {
        setCartError('Invalid quantity');
        return;
      }

      dispatch(
        addToCart({
          name: product.name,
          price: product.price.toString(),
          image: product.image_product,
          quantity: parsedQuantity,
          product: product.id,
          weight: product.weight,
        })
      );
    } else {
      SweetAlert.error(
        'Error',
        'Anda harus masuk terlebih dahulu untuk menambahkan produk ke keranjang.'
      );
    }
  };

  useEffect(() => {
    if (slug) {
      dispatch(fetchProductBySlug(slug));
    }
  }, []);

  return (
    <div className="max-w-screen-xl mx-auto mt-10">
      {loading ? (
        <LoadingIndicator />
      ) : error ? (
        <IsError error={error} />
      ) : (
        <>
          {product && (
            <div key={product.id}>
              <div className="flex flex-col md:flex-row">
                <div className="md:w-1/2">
                  <div className="bg-white p-4 rounded-md shadow-md">
                    <img
                      src={product.image_product}
                      alt={product.name}
                      className="w-full h-auto"
                      width={100}
                      height={100}
                    />
                  </div>
                </div>
                <div className="md:w-1/2 md:pl-8 mt-4 md:mt-0">
                  <h1 className="text-xl xl:text-2xl font-medium mb-1">
                    {product.name}
                  </h1>

                  <div className="bg-white p-4 rounded-md shadow-md">
                    <h2 className="text-lg font-medium mb-2">
                      Product Description
                    </h2>
                    <p>{product.description}</p>
                  </div>

                  <div className="mt-4">
                    <h2 className="text-lg font-medium mb-2">Brand</h2>
                    <div className="bg-blue-100 text-blue-800 py-2 px-4 rounded-lg">
                      {product.brand}
                    </div>
                  </div>

                  <div className="bg-white p-4 rounded-md shadow-md mt-10">
                    <div className="m-2">
                      <h1 className="text-lg font-medium mb-2">Price:</h1>
                      <p>{product.price}</p>
                    </div>
                    <hr />
                    <div className="m-2">
                      <h1 className="text-lg font-medium mb-2">
                        Selected Quantity:
                      </h1>
                      <select
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                      >
                        {[...Array(product.countInStock).keys()].map((x, i) => {
                          return <option value={i + 1}>{i + 1}</option>;
                        })}
                      </select>
                    </div>
                    <hr />
                    {product.countInStock > 0 ? (
                      <button
                        className="bg-gray-800 text-white py-2 px-4 rounded-md mt-6"
                        onClick={addCart}
                      >
                        Add to Cart
                      </button>
                    ) : (
                      <div className="m-2">
                        <h1>Out Of Stock</h1>
                        <button
                          className="bg-gray-300 text-gray-500 py-2 px-4 rounded-md cursor-not-allowed mt-2"
                          disabled
                        >
                          Add to Cart
                        </button>
                      </div>
                    )}
                  </div>
                  <div className="mt-10">
                    <Review product={product} />
                  </div>
                </div>
              </div>
            </div>
          )}
        </>
      )}

      {cartError && <Error error={cartError} />}
    </div>
  );
}
