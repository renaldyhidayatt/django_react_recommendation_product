import { useEffect } from 'react';
import Slider from '../components/Sliders';
import { fetchAllSliders } from '../redux/slider.slice';
import { useDispatch, useSelector } from 'react-redux';
import Category from '../components/Category';
import { fetchAllCategories } from '../redux/category.slice';
import Product from '../components/Product';
import { fetchProducts } from '../redux/product.slice';


export default function Home() {
    const myslider = useSelector((state) => state.sliderReducer);
    const mycategory = useSelector((state) => state.categoryReducer);
    const myproduct = useSelector((state) => state.productReducer);

    const dispatch = useDispatch();

    const { loading: loadingProduct, error: errorProduct, products } = myproduct;

    const { loading: loadingCat, error: errorCat, categories } = mycategory;

    const { loading, sliders, error } = myslider;

    const isLoading = loading || loadingProduct || loadingCat;
    const isError = error || errorProduct || errorCat;


    useEffect(() => {


        dispatch(fetchAllCategories());
        dispatch(fetchAllSliders());
        dispatch(fetchProducts());

    }, []);

    return (
        <>
            {isLoading ? (
                <h1>Loading</h1>
            ) : isError ? (
                <h1>Error</h1>
            ) : (
                <>
                    <Slider sliders={sliders} />
                    <Category categories={categories} />
                    <Product products={products} />
                </>
            )}
        </>
    );
}