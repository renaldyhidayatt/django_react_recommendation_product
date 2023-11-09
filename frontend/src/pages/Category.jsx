import { useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { fetchCategoryBySlug } from '../redux/category.slice';
import { useDispatch, useSelector } from 'react-redux';
import { Rating, Star } from '@smastrom/react-rating';

const myStyles = {
  itemShapes: Star,
  activeFillColor: '#ffb700',
  inactiveFillColor: '#fbf1a9',
};

export default function CategoryPage() {
  const { slug } = useParams();
  const category = useSelector((state) => state.categoryReducer.category);
  const loading = useSelector((state) => state.categoryReducer.loading);
  const error = useSelector((state) => state.categoryReducer.error);
  const dispatch = useDispatch();

  useEffect(() => {
    if (slug) {
      dispatch(fetchCategoryBySlug(slug));
    }
  }, [dispatch, slug]);

  return (
    <div className="max-w-screen-xl mx-auto mt-10">
      {!loading && error && (
        <h1 className="text-2xl font-semibold p-3">Error: {error}</h1>
      )}
      {!loading && !error && !category && (
        <h1 className="text-2xl font-semibold p-3">No category found</h1>
      )}
      {!loading && !error && category && category.products && (
        <>
          <h1 className="text-2xl font-semibold p-3">{category.name}</h1>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
            {category.products.map((product) => (
              <Link
                to={`/product/${product.slug_product}`}
                key={product.product_id}
                className="sm:col-span-1 md:col-span-1 lg:col-span-1"
              >
                <div className="p-4 border rounded-lg shadow-md bg-white">
                  <div className="relative overflow-hidden">
                    <img
                      src={`${product.image_product}`}
                      className="w-full h-40 object-cover rounded-lg"
                      alt={product.name}
                    />
                  </div>
                  <div className="mt-4">
                    <Rating
                      value={product.rating}
                      readOnly={true}
                      itemStyles={myStyles}
                      style={{ maxWidth: 250 }}
                    />
                    <h3 className="text-lg font-semibold text-gray-800">
                      {product.name}
                    </h3>
                    <p className="mt-1 text-gray-600">{product.description}</p>
                    <p className="mt-2 text-gray-800 font-semibold">
                      Rp. {product.price}
                    </p>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </>
      )}
      {loading && <h1>Loading...</h1>}
    </div>
  );
}
