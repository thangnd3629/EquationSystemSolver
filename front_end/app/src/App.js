import React, { Component } from "react";
import "./App.css";
import Progress from './progress/Progress'
import Upload from "./upload/Upload";
import { Button ,Modal} from 'react-bootstrap';
class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="Card_main">
          <Upload />
          
          
        </div>
      </div>
    );
  }
}

export default App;
