import React, {Component} from 'react';
import Banner from "./Banner";
import {Divider} from "antd";
import VideoList from "./VideoList";

class Home extends Component {
    render() {
        return (
            <div>
                <Banner/>
                <div className="container my-4">
                    <h3>Processed Videos</h3>
                    <Divider/>
                    <VideoList/>
                </div>
            </div>
        );
    }
}

export default Home;