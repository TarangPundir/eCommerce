import React, { useState } from 'react';
import RemoveCircleIcon from '@mui/icons-material/RemoveCircle';
import AddCircleIcon from '@mui/icons-material/AddCircle';


let MyAccordisn = ({ questions, answers }) => {
    let [show, setshow] = useState(false);
    let [sign, setsign] = useState(false)

    let ShowHide = () => {
        setshow(!show)
        setsign(!sign)
    }
    return (
        <> <div className="_question" onClick={ShowHide}>
            <h1 className="Symbol" >{sign ? <RemoveCircleIcon /> : <AddCircleIcon />} </h1>
            <h1 className="question">{questions}</h1>
        </div>
            <div className="_answer">
                <p className="answer" style={{ display: show ? "" : "none" }} >{answers}</p>
            </div>

        </>
    )
}
export default MyAccordisn