import ModalCategory from './Category';
import ModalProduct from './Product';
import ModalSlider from './Slider';
import ModalUser from './User';

export default function Modal() {
  return (
    <>
      <ModalCategory />
      <ModalProduct />
      <ModalSlider />
      <ModalUser />
    </>
  );
}
