import React, {Component} from 'react';
import {Layout} from 'antd';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

import Home from "./components/Home";
import VideoPage from "./components/VideoPage";

import './App.scss';

const {Header, Content, Footer} = Layout;

class App extends Component {
    render() {
        return (
            <Layout className="custom_layout">
                <Header>
                    <div className="logo">

                    </div>
                </Header>
                <Content>
                    <Router>
                        <Switch>
                            <Route path='/' exact component={Home}/>
                            <Route path='/video/:id' exact component={VideoPage}/>
                        </Switch>
                    </Router>
                </Content>
                <Footer style={{textAlign: 'center'}}>
                    Created by Bawana Bois
                </Footer>
            </Layout>
        );
    }
}

export default App;
