import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import RemoveShoppingCartIcon from '@mui/icons-material/RemoveShoppingCart';


const NavBar = () => {
    let [show, hide] = useState(false)
    let showData = () => {
        if (show === false) {
            hide(true)
        }
        else {
            hide(false)
        }
    }
    let hideData = () => {
        hide(false)
    }
    return (
        <>
            <div className='main_nav'>
                <div className='icon_div'>
                    <NavLink className='icon_link' to='' >Two Fifteen</NavLink>
                </div>
                <div className='nav_option'>
                    <NavLink className='link_option' to='' >Home</NavLink>
                    <div className='link_option' onClick={showData}>Category</div>
                    <NavLink className='link_option' to='/contactus' >Contact-Us</NavLink>
                    <NavLink className='link_option' to='/aboutus' >About-us</NavLink>
                    <NavLink className='link_option' to='/login' >Login</NavLink>
                    <div type="button" className='link_option' data-bs-toggle="modal" data-bs-target="#exampleModal">
                        <AddShoppingCartIcon />
                    </div>

                </div>
            </div>

            {show ? <div className='category_ooptions' >
                <NavLink className='category_link' onClick={hideData} to='/category/electronic'>Electronics</NavLink>
                <NavLink className='category_link' onClick={hideData} to='/category/fashion'>Fashion</NavLink>
                <NavLink className='category_link' onClick={hideData} to='/category/skincare'>Skincare</NavLink>
            </div> : null}

            <div className="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div className="modal-dialog">
                    <div className='cart_main_body'>
                        <div className='cart_component'>
                            <div className='cart_img_div'>
                                <img className='cart_img' src="" alt="" />
                            </div>
                            <div className='Cart_product_info'>
                                <h4 className='cart_product_name' >product</h4>
                                <p className='cart_product_description'>description</p>
                                <p className='cart_product_price'>500</p>
                            </div>
                            <div className='cart_buy_options'>
                                <button >
                                    <ShoppingCartIcon />
                                </button>
                                <br />
                                <br />
                                <button>
                                    <RemoveShoppingCartIcon />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </>
    )
}
export default NavBar