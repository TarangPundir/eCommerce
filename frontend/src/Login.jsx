import React, { useState } from 'react';


const Login = () => {
    let [formData, setFormData] = useState({
        username: "",
        password: ""

    })
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!formData.username || !formData.password) {
            alert('Please enter all required credentials')
        } else {
            alert('you are loged in')
            setFormData({
                username: "",
                password: ""
            })
        }
    };
    return (
        <>
            <div className='login_form'>
                <div className='contactus_form_div'>
                    <h1 className='log_in'>Log In</h1>
                </div>
                <form onSubmit={handleSubmit}>
                    <div className='input_ligin'>
                        <div className='login_input_div'>

                            <input className='login_input' type="text" placeholder='username' name='username' value={formData.username} onChange={handleChange} />
                        </div>
                        <div className='login_input_div'>

                            <input className='login_input' type="password" placeholder='password' name='password' value={formData.password} onChange={handleChange} />
                        </div>

                    </div>
                    <button type='submit' className='btn btn-primary mt-5' style={{ marginLeft: "204px" }}>Submit</button>
                </form>
            </div>
        </>
    )
}
export default Login;