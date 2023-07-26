import React, { useState } from 'react';

const Contactus = () => {
    let [formData, setFormData] = useState({
        firstname: "",
        email: "",
        textarea: ""
    })

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!formData.firstname || !formData.email || !formData.textarea) {
            alert('Please enter all required credentials');
        } else {
            console.log('Form data submitted:', formData);
            setFormData({
                firstname: "",
                email: "",
                textarea: ""
            })
        }
    };
    return (
        <>
            <div className='contactus_main'>
                <div id="carouselExampleIndicators" className="carousel slide " style={{ boxShadow: "#5e505047 0px 4px 53px 5px;" }}  >
                    <div className="carousel-indicators">
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <img src="https://st4.depositphotos.com/13193658/28578/i/450/depositphotos_285780842-stock-photo-selective-focus-cheerful-blonde-operator.jpg" className="d-block w-100 contactus_image" alt="..." />
                        </div>
                        <div className="carousel-item">
                            <img src="https://st3.depositphotos.com/1001877/32125/i/450/depositphotos_321258156-stock-photo-contact-us-website-page-on.jpg" className="d-block w-100 contactus_image" alt="..." />
                        </div>
                        <div className="carousel-item">
                            <img src="https://st2.depositphotos.com/1265075/7826/i/450/depositphotos_78262052-stock-photo-contact-us-icons-web-connection.jpg" className="d-block w-100 contactus_image" alt="..." />
                        </div>
                    </div>
                    <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Previous</span>
                    </button>
                    <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Next</span>
                    </button>
                </div>
                <div className='contactus_form'>
                    <div className='contactus_form_div'>
                        <h1 className='Contact_us'>Contact Us</h1>
                    </div>
                    <form onSubmit={handleSubmit}>
                        <div className='input_contact'>
                            <div className='contactus_input_div'>
                                <h1 className='lable'>Enter Your Name:-</h1>
                                <input type="text" placeholder='enter your name' name='firstname' value={formData.firstname} onChange={handleChange} />
                            </div>
                            <div className='contactus_input_div'>
                                <h1 className='lable'>Enter Your Email:-</h1>
                                <input type="email" placeholder='enter your email' name='email' value={formData.email} onChange={handleChange} />
                            </div>
                            <div className='contactus_input_div'>
                                <h1 className='lable'>Enter description:-</h1>
                                <textarea name="textarea" placeholder='enter description ...' value={formData.textarea} onChange={handleChange}></textarea>
                            </div>
                        </div>
                        <button type='submit' className='btn btn-primary mt-5' style={{ marginLeft: "204px" }}>Submit</button>
                    </form>
                </div>
            </div>
        </>
    )
}
export default Contactus;


