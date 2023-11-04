import { Link } from 'react-router-dom';

export default function Category({ categories }) {
    return (
        <div className="max-w-screen-xl mx-auto mt-10">
            <div className="mt-10">
                <h1 className="text-2xl font-semibold p-3">Category</h1>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-4 md:grid-cols-4 lg:grid-cols-4 xl:grid-cols-4 gap-6 mt-10">
                {categories.length > 0 ? (
                    categories.map((category) => (
                        <Link
                            key={category.id}
                            to={'/category/' + category.slug_category}
                            className="p-2 border rounded-lg shadow"
                        >
                            <div className="flex items-center justify-center h-24">
                                <img
                                    src={category.image_category}
                                    alt={category.name}
                                    className="h-16 w-auto max-w-full"
                                />
                            </div>
                            <div className="mt-2 text-center">
                                <h4 className="text-base sm:text-lg md:text-lg lg:text-lg">
                                    {category.name}
                                </h4>
                            </div>
                        </Link>
                    ))
                ) : (
                    <p>No categories available.</p>
                )}
            </div>
        </div>
    );
}
