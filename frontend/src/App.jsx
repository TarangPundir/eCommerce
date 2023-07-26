import React, { Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Contactus from './contactus';
import Aboutus from './Aboutus';
import Login from './Login';
import Electronic from './Electronics';
import Fashion from './Fashion';
import Skincare from './Skincare';
import NavBar from './NavBar';

const App = () => {
    return (
        <>
            <NavBar />
            <Suspense>
                <Routes>
                    <Route path='' element={<Home />} />
                    <Route path='/contactus' element={<Contactus />} />
                    <Route path='/aboutus' element={<Aboutus />} />
                    <Route path='/login' element={<Login />} />
                    <Route path='/category/electronic' element={<Electronic />} />
                    <Route path='/category/fashion' element={<Fashion />} />
                    <Route path='/category/skincare' element={<Skincare />} />
                </Routes>
            </Suspense >
        </>
    )
}
export default App