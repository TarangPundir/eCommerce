import React from 'react';
import { NavLink } from 'react-router-dom';

const HomeCategory = () => {
    return (
        <>
            <div className='home_category'>
                <NavLink className='home_category_options' to='/category/electronic'>
                    <div className='electronics'>
                        <h1 className='home_category_heading'>
                            Electronics
                        </h1>
                    </div>
                </NavLink>
                <NavLink className='home_category_options' to='/category/fashion'>
                    <div className='fashion'>
                        <h1 className='home_category_heading'>
                            Fashion
                        </h1>
                    </div>
                </NavLink>
                <NavLink className='home_category_options' to='/category/skincare'>
                    <div className='skincare'>
                        <h1 className='home_category_heading'>
                            SkinCare
                        </h1>
                    </div>
                </NavLink>
            </div >
        </>
    )
}
export default HomeCategory