import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { updateUser } from '../../redux/user.slice';
import { LoadingIndicator } from '../../components/Loading';
import { IsError } from '../../components/ISError';
import ISSuccess from '../../components/IsSuccess';

export default function ProfilePage() {
    const updateState = useSelector((state) => state.updateUserReducer);
    const user = useSelector((state) => state.authReducer.user);

    const { loading, success, error } = updateState;
    const dispatch = useDispatch();
    const [firstname, setFirstName] = useState(user.firstname);
    const [lastname, setLastName] = useState(user.lastname);
    const [email, setEmail] = useState(user.email);
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    function handleUpdate(e) {
        e.preventDefault();
        if (password === confirmPassword) {
            const updatedUser = {
                name,
                email,
                password,
            };
            dispatch(updateUser(user.id, updatedUser));
        } else {
            alert('Passwords do not match');
        }
    }


    return (
        <div className="justify-center mt-8">
            <div className="w-2/3 mx-auto bg-white shadow p-6 rounded">
                <h2 className="text-center mb-6">Update</h2>

                {loading && <LoadingIndicator />}
                {error && <IsError error="Something went wrong" />}
                {success && (
                    <ISSuccess success="Your details have been updated successfully. Please re-login." />
                )}

                <form className="space-y-4" onSubmit={handleUpdate}>
                    <div>
                        <label htmlFor="name" className="block mb-2 font-medium">
                            Firstname
                        </label>
                        <input
                            type="text"
                            id="name"
                            placeholder="Name"
                            className="w-full p-2 border border-gray-300 rounded"
                            required
                            value={firstname}
                            onChange={(e) => setFirstName(e.target.value)}
                        />
                    </div>
                    <div>
                        <label htmlFor="name" className="block mb-2 font-medium">
                            Lastname
                        </label>
                        <input
                            type="text"
                            id="name"
                            placeholder="Name"
                            className="w-full p-2 border border-gray-300 rounded"
                            required
                            value={lastname}
                            onChange={(e) => setLastName(e.target.value)}
                        />
                    </div>

                    <div>
                        <label htmlFor="email" className="block mb-2 font-medium">
                            Email
                        </label>
                        <input
                            type="text"
                            id="email"
                            placeholder="Email"
                            className="w-full p-2 border border-gray-300 rounded"
                            value={email}
                            required
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>

                    <div>
                        <label htmlFor="password" className="block mb-2 font-medium">
                            Password
                        </label>
                        <input
                            type="password"
                            id="password"
                            placeholder="Password"
                            className="w-full p-2 border border-gray-300 rounded"
                            value={password}
                            required
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>

                    <div>
                        <label htmlFor="confirmPassword" className="block mb-2 font-medium">
                            Confirm Password
                        </label>
                        <input
                            type="password"
                            id="confirmPassword"
                            placeholder="Confirm Password"
                            className="w-full p-2 border border-gray-300 rounded"
                            value={confirmPassword}
                            required
                            onChange={(e) => setConfirmPassword(e.target.value)}
                        />
                    </div>

                    <div className="text-right">
                        <button
                            type="submit"
                            className="bg-blue-500 text-white px-4 py-2 rounded"
                        >
                            UPDATE
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
