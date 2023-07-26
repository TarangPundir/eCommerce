import React from 'react';

let About_us_banner = () => {
    return (
        <>
            <div id="carouselExampleCaptions" className="carousel slide">
                <div className="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div className="carousel-inner">
                    <div className="carousel-item active">
                        <img style={{ height: '550px' }} src="https://st3.depositphotos.com/1022914/16288/i/1600/depositphotos_162882256-stock-photo-amazon-com-logo-on-the.jpg" className="d-block w-100" alt="..." />
                        <div className="carousel-caption d-none d-md-block">
                            <h5>First slide label</h5>
                            <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <img style={{ height: '550px' }} src="https://st2.depositphotos.com/1083585/9858/i/950/depositphotos_98586104-stock-photo-amazon-logotype-printed-on-cardboard.jpg" className="d-block w-100" alt="..." />
                        <div className="carousel-caption d-none d-md-block">
                            <h5>Second slide label</h5>
                            <p>Some representative placeholder content for the second slide.</p>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <img style={{ height: '550px' }} src="https://st4.depositphotos.com/3317865/22937/i/1600/depositphotos_229373614-stock-photo-szczecin-poland-november-2018-amazon.jpg" className="d-block w-100" alt="..." />
                        <div className="carousel-caption d-none d-md-block">
                            <h5>Third slide label</h5>
                            <p>Some representative placeholder content for the third slide.</p>
                        </div>
                    </div>
                </div>
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>

            <div className='about_text'>
                <h1>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae, autem?</h1>
                <p className='paragraph_about'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolore magnam fugiat dolorem provident architecto vel inventore est aliquid laudantium molestias quo vero necessitatibus, dicta aut neque a, nesciunt facere praesentium quod, animi voluptatibus doloremque! Autem atque accusantium saepe sapiente placeat alias neque tempora dolor, consequatur, omnis repudiandae odit ullam sint dolores aliquam blanditiis incidunt, ipsum quibusdam porro unde non. Cupiditate voluptates soluta dolorum nobis cum impedit sunt maiores doloribus id perferendis iusto qui placeat assumenda, veritatis magnam temporibus laboriosam enim, deserunt esse error molestiae consectetur culpa. Officia dolor sit rem corporis iste voluptas debitis accusantium. Vitae fugiat adipisci autem, quod, nulla similique soluta et magni, animi aliquam officia tempore maiores quo vero iste eligendi sequi! Nesciunt cum temporibus facere ipsam.</p>
            </div>
        </>
    )
}

export default About_us_banner