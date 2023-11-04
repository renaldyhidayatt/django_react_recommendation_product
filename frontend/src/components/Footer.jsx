import { Link } from 'react-router-dom';

export default function Footer() {
    return (
        <footer className="bg-white dark:bg-[#1c1d1f] rounded-lg shadow-lg fixed bottom-0 w-full">
            <div className="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
                <span className="text-sm text-gray-500 sm:text-center dark:text-gray-400">
                    © 2023{' '}
                    <Link href="#" className="hover:underline">
                        Renaldy Hidayat™
                    </Link>
                    . All Rights Reserved.
                </span>
                <ul className="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0 md:flex-row">
                    <li>
                        <Link href="#" className="mr-4 hover:underline md:mr-6">
                            About
                        </Link>
                    </li>
                    <li>
                        <Link href="#" className="mr-4 hover:underline md:mr-6">
                            Privacy Policy
                        </Link>
                    </li>
                    <li>
                        <Link href="#" className="mr-4 hover:underline md:mr-6">
                            Licensing
                        </Link>
                    </li>
                    <li>
                        <Link href="#" className="hover:underline">
                            Contact
                        </Link>
                    </li>
                </ul>
            </div>
        </footer>

    );
}