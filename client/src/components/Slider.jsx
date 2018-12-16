import React, {Component} from 'react';
import {Carousel} from "antd";

class Slider extends Component {
    render() {
        return (
            <Carousel>
                <div>
                    {/*// Checkout Impress Js*/}
                    <h3 className='title'>Title</h3>
                </div>
                <div><h3>2</h3></div>
                <div><h3>3</h3></div>
                <div><h3>4</h3></div>
            </Carousel>
        );
    }
}

export default Slider;