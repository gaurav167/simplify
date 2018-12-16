import React, {Component} from 'react';

import {List, Col, Row, Icon} from 'antd';
import {Link} from 'react-router-dom';

const listData = [];
for (let i = 0; i < 23; i++) {
    listData.push({
        href: 'http://ant.design',
        title: `Video ${i}`,
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        description: 'Author of Video',
        content: 'Some Lorem Ispum Random Ass COntent Proably more than 1 paragraph  from summarized text or yotube description tent Proably more than 1 paragraph  from summarized text or yotube description tent Proably more than 1 paragraph  from otube descriptiontent Proably more than 1 paragraph  from summarized text or yotube description',
    });
}

const IconText = ({type, text}) => (
    <span>
        <Icon type={type} style={{marginRight: 8}}/>
        {text}
    </span>
);


class VideoList extends Component {
    render() {
        return (
            <div className='video-list'>
                <List
                    itemLayout="vertical"
                    size="large"
                    pagination={{
                        onChange: (page) => {
                            console.log(page);
                        },
                        pageSize: 5,
                    }}
                    dataSource={listData}
                    footer={<div><b>Some Footer</b> Text</div>}
                    renderItem={item => (
                        <List.Item key={item.title}>

                            <Row gutter={16} className='flex-row'>

                                <Col span={6}>
                                    <Link to={'/video'}>
                                        <div>
                                            <img className='img-fluid'
                                                 src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
                                                 alt=""/>
                                        </div>
                                    </Link>
                                </Col>
                                <Col span={18}>
                                    <div>
                                        <Link to={'/video'}>
                                            <List.Item.Meta
                                                title={item.title}
                                                description={item.description}
                                            />
                                        </Link>
                                        {item.content}

                                        <div className="actions">
                                            <ul>
                                                <li>
                                                    <IconText type="star-o" text="156"/>
                                                </li>
                                                <li>
                                                    <IconText type="like-o" text="156"/>
                                                </li>
                                                <li>
                                                    <IconText type="message" text="2"/>
                                                </li>
                                            </ul>

                                        </div>

                                    </div>
                                </Col>
                            </Row>
                        </List.Item>
                    )}
                />

            </div>
        );
    }
}

export default VideoList;