import React, { Component } from "react";
import { Modal, Button } from 'react-bootstrap';
import 'katex/dist/katex.min.css';
import { BlockMath, InlineMath } from 'react-katex';
import './Mathdisplay.css'
const MathDisplay = (props) => {
    var eq_list = props.eqs

    var res_list = props.res

    var place_holder_eqs = String.raw``;
    var place_holder_res = String.raw``;

    eq_list.map((elm) => {
        place_holder_eqs = place_holder_eqs + String.raw`${elm}`
        place_holder_eqs = place_holder_eqs + String.raw`\\`
    })
    res_list.map((elm) => {
        var symbol = Object.keys(elm)

        symbol.forEach((element) => {
            place_holder_res += String.raw`& ${element} =  ${elm[element]} & `
        })
        place_holder_res += String.raw`\\`
        
    })
    var eq_list_raw_string = String.raw`\begin{cases}
                                            ${place_holder_eqs}
                                            
                                            \end{cases}`;
    var res_list_raw_string = String.raw`\begin{bmatrix}
                                    ${place_holder_res}
    
                                    \end{bmatrix}`
    return (

        <Modal show={props.show} onHide={props.handleCloseModal} dialogClassName="my-modal" >
            <Modal.Header closeButton>
                <Modal.Title>Result</Modal.Title>
            </Modal.Header>
            <Modal.Body>

                <div>
                    
                    <img src={"data:image/jpg;base64," + props.original_img} style={{border: '3px solid red',borderRadius: "20px"}} />
                    <InlineMath math={String.raw`\Longrightarrow`}></InlineMath>
                    <img src={"data:image/jpg;base64," + props.deskewed_img} style={{border: '3px solid cyan',borderRadius: "40px"}} />
                    <InlineMath math={String.raw`\Longrightarrow`}></InlineMath>
                    <img src={"data:image/jpg;base64," + props.cropped_img}   style={{border: '3px solid green',borderRadius: "100px"}}/>
                    <div class="container">
                        <div className="row">
                            
                        </div>
                        <div class="row">
                            <div class="col">
                                <BlockMath math={String.raw`\text{Detected Equation System}`}></BlockMath>
                                <BlockMath
                                    math={eq_list_raw_string}></BlockMath>
                            </div>
                            <div class="col">
                                <BlockMath math={String.raw`\text{Solution(s)}`}></BlockMath>
                                <BlockMath
                                    math={res_list_raw_string}>

                                </BlockMath>
                            </div>
                        </div>

                    </div>
                </div>



            </Modal.Body>

        </Modal>







    );
}
export default MathDisplay