import React, { useState } from 'react';
import Sdata from './About_accordian_api';
import MyAccordisn from './MyAccoedian';
let ABoutAccordian = () => {
    let [acc, setAcc] = useState(Sdata)
    return (
        <>
            <div className='about_acc'>
                {acc.map((cuData) => {
                    let { id } = cuData
                    return <MyAccordisn key={id} {...cuData}/>
                })}
            </div>
        </>
    )
}
export default ABoutAccordian