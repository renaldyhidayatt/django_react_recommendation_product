import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Autoplay } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/navigation';

export default function Slider({ sliders }) {
    return (
        <>
            <div className="mx-auto flex justify-center mt-10">
                <Swiper
                    loop={true}
                    spaceBetween={0}
                    navigation={true}
                    modules={[Navigation, Autoplay]}
                    className="relative h-56 sm:h-72 md:h-96 w-full sm:w-10/12 md:w-11/12 lg:w-8/12 xl:w-7/12 2xl:w-6/12 overflow-hidden rounded-lg "
                    style={{ borderRadius: '10px' }}
                >
                    {sliders.map((slider) => (
                        <SwiperSlide key={slider.id}>
                            <img src={slider.image} alt={slider.nama} />
                        </SwiperSlide>
                    ))}
                </Swiper>
            </div>
        </>
    );
}