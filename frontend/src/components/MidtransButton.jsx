import React, { useEffect } from 'react';

const CLIENT_KEY = import.meta.env.VITE_MIDTRANS_CLIENT_KEY;

const MidtransPaymentButton = ({ handlePayment, disabled }) => {
    useEffect(() => {
        const snapSrcUrl = 'https://app.sandbox.midtrans.com/snap/snap.js';
        const myMidtransClientKey = `${CLIENT_KEY}`;
        const script = document.createElement('script');
        script.src = snapSrcUrl;
        script.setAttribute('data-client-key', myMidtransClientKey);
        script.async = true;

        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        };
    }, []);

    return (
        <button
            className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
            onClick={handlePayment}
            disabled={disabled}
        >
            PAY
        </button>
    );
};

export default MidtransPaymentButton;