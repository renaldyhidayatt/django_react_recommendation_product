import { Link } from 'react-router-dom';
import { Rating, Star } from '@smastrom/react-rating';
import { slice } from 'lodash';

const myStyles = {
  itemShapes: Star,
  activeFillColor: '#ffb700',
  inactiveFillColor: '#fbf1a9',
};

export default function Product({ products }) {
  return (
    <div className="max-w-screen-xl mx-auto mt-10">
      <div className="mt-10">
        <h1 className="text-2xl font-semibold p-3">Product</h1>
      </div>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        {products.length > 0 ? (
          products.map((row) => (
            <Link to={`/product/${row.slug_product}`} key={row.id}>
              <div className="p-4 border rounded-lg shadow-md bg-white">
                <div className="relative overflow-hidden">
                  <img
                    src={row.image_product}
                    alt={row.name}
                    className="w-full h-32 sm:h-40 object-cover rounded-lg"
                  />
                </div>
                <div className="mt-4">
                  <Rating
                    value={row.rating}
                    readOnly={true}
                    itemStyles={myStyles}
                    style={{ maxWidth: 250 }}
                  />
                  <h3 className="text-lg font-semibold text-gray-800">
                    {row.name}
                  </h3>

                  <p className="mt-2 text-gray-800 font-semibold">
                    Rp. {row.price.toLocaleString()}
                  </p>
                </div>
              </div>
            </Link>
          ))
        ) : (
          <p>Not found</p>
        )}
      </div>
    </div>
  );
}
