import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

let Sliders = () => {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        prevArrow: <span className="slider-arrow prev"></span>,
        nextArrow: <span className="slider-arrow next"></span>,
        autoplay: true,
        autoplaySpeed: 1000,
    };
    return (
        <>
            <div id="carouselExampleSlidesOnly" className="carousel slide mt-5" style={{ boxShadow: "#00000038 0px 4px 53px 5px", paddingTop: "30px", paddingBottom: "30px",overflowX: "hidden" }} data-ride="carousel">
                <Slider {...settings}>
                    <div>
                        <div className='slider'>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div className='slider'>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div className='slider'>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                            <div className="card" style={{ width: "18rem", paddingTop: "20px", paddingBottom: '20px' }}>
                                <img src="..." className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </Slider>
            </div>
        </>
    )
}
export default Sliders