import Swal from 'sweetalert2';

const SweetAlert = {
  success: (title, text) => {
    return Swal.fire({
      icon: 'success',
      title: title,
      text: text,
    });
  },
  error: (title, text) => {
    return Swal.fire({
      icon: 'error',
      title: title,
      text: text,
    });
  },
  confirm: (title, text) => {
    return Swal.fire({
      icon: 'info',
      title: title,
      text: text,
    });
  },
};

export default SweetAlert;
