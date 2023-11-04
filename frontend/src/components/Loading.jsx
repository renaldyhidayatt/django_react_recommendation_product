export const LoadingIndicator = () => {
    return (
        <div className="flex items-center justify-center">
            <svg
                aria-hidden="true"
                className="w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                viewBox="0 0 100 101"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            ></svg>
            <span className="sr-only">Loading...</span>
        </div>
    );
};