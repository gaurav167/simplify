import React, {Component} from 'react';
// import {Row, Col} from 'antd';
// import Banner from "./Banner";
// import VideoList from "./VideoList";
import {Divider, List} from "antd";
import data from './data' ;

class VideoPage extends Component {

    state = {
        readMore: false
    };

    componentWillMount() {
        let id = this.props.match.params.id;
        this.setState({id: id});

        data.forEach(item => {
            if (item.id == id) {
                console.log(true);
                this.setState({video: item});
            }
        });


    }

    componentDidMount() {

        console.log(this.state.video);
        this.readTextFile(`/assets/${this.state.video.id}.txt`);
    }

    convertToMinutes(seconds) {
        let date = new Date(null);
        date.setSeconds(seconds); // specify value for SECONDS here
        let result = date.toISOString().substr(11, 8);
        return result;
    }

    readTextFile = file => {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET", file, false);
        rawFile.onreadystatechange = () => {
            if (rawFile.readyState === 4) {
                if (rawFile.status === 200 || rawFile.status == 0) {
                    var allText = rawFile.responseText;
                    this.setState({
                        text: allText
                    });
                }
            }
        };
        rawFile.send(null);
    };

    render() {

        if (!this.state.id) {
            return <div/>;
        }

        let video = this.state.video;

        if (!video) {
            return <div/>;
        }


        return (
            <div>
                <div className="my-4 video-player-container">
                    <div className="video-player">
                        <div className="sixteen-nine">
                            <div className="content slider">
                                <div className="video">
                                    <video controls>
                                        <source src={`/assets/${video.id}.mp4`} type="video/mp4"/>
                                        Your browser does not support the video tag.
                                    </video>
                                </div>
                            </div>
                        </div>
                        <div className="video-summary">
                            <div className="title-block">
                                <h4>
                                    {video.name}
                                </h4>
                                <h6>Taught By : {video.author}</h6>
                            </div>
                            <Divider/>
                            <div className="summary-block">
                                <div>
                                    {this.state.text && (
                                        this.state.text.split("\n").map((item, key) => {
                                            if (this.state.readMore) {
                                                if ((key + 1) % 7 === 0) {
                                                    return <span key={key}>{item}<br/> <br/></span>;
                                                }
                                                return <span key={key}>{item}&nbsp;</span>;
                                            } else {
                                                if (key < 7) {
                                                    return <span key={key}>{item}&nbsp;</span>;
                                                }
                                                if (key === 7) {
                                                    return <span>
                                                        <br/><br/>
                                                        <span className='read-more' onClick={() => {
                                                            this.setState({readMore: true});
                                                        }}>
                                                            Read More
                                                        </span>
                                                    </span>;
                                                }
                                            }

                                        })
                                    )}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="video-player-sidebar">
                        <div className="video-button-options">
                            <div className="option-1 toc">
                                <List
                                    size="large"
                                    header={<div className='toc-heading'>Table of Contents</div>}
                                    bordered
                                    dataSource={video.toc}
                                    renderItem={item => (
                                        <List.Item>
                                            <div class="toc-body">
                                                <a href={`${video.url}${item.timestamp}`} target="_blank">
                                                    <span>{item.heading}</span>
                                                    <span className="right-align">
                                                        {this.convertToMinutes(item.timestamp)}
                                                    </span>
                                                </a>
                                            </div>
                                        </List.Item>
                                    )}
                                />
                            </div>
                            <div className="option-1 toc"
                                 style={{
                                     minHeight: 100,
                                     lineHeight: '100px',
                                     textAlign: 'center'
                                 }}>
                                <a href={video.url} target="_blank">
                                    <div className="toc-body">
                                        View Original Video
                                    </div>
                                </a>
                            </div>
                        </div>
                        {/*<div className="video-related-list">*/}

                        {/*</div>*/}
                    </div>
                </div>


            </div>
        );
    }
}

export default VideoPage;