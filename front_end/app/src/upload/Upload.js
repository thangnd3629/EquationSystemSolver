import React, { Component } from "react";
import Dropzone from "../dropzone/Dropzone";
import "./Upload.css";
import Progress from "../progress/Progress";
import axiosInstance from '../axios'
import MathDisplay from '../mathdisplay/Mathdisplay'

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false,
      deskewed_img : null,
      cropped_img:null,
      original_img:null,
      eq_list : null,
      result : null,
      show_result_modal : false
    };

    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  onFilesAdded(files) {
    this.setState({ files: [].concat(files) });
  }
  sendRequest() {
    this.setState({uploading:true})
    var file = this.state.files[0]
    const formData = new FormData();
    formData.append("file", file, file.name);

    
    let config = {
      onUploadProgress: progressEvent => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = {
          state: "pending",
          percentage: Math.floor((progressEvent.loaded * 100) / progressEvent.total)
        };
        this.setState({ uploadProgress: copy });
      }
    }
    axiosInstance.post("http://127.0.0.1:5000/", formData, config)
      .then(response => {
        console.log(response)
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy });
        this.setState({ successfullUploaded: true, uploading: false });
        this.setState({cropped_img: response.data['cropped_eq']})
        this.setState({deskewed_img: response.data['deskewed_img']})
        this.setState({original_img: response.data['original_img']})
        this.setState({eq_list:response.data['list_eqs']})
        this.setState({result:response.data['result']})
      }
      )
      .catch(err => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        console.log(err)
      })

  }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        
          <Progress done={uploadProgress ? uploadProgress.percentage : 0} />
          
        
      );
    }
  }

  renderActions() {
    if (this.state.successfullUploaded) {
      return (
        <button
          onClick={() =>
            this.setState({ files: [], successfullUploaded: false })
          }
        >
          Clear
        </button>
      );
    } else {
      return (
        <button
          disabled={this.state.files.length === 0 || this.state.uploading}
          onClick={this.sendRequest}
        >
          Upload
        </button>
      );
    }
  }
  handleCloseModal = () => {
    this.setState({result:null})
    this.setState({uploading:false})
    this.setState({successfullUploaded:false})
  }

  render() {
    
    return (
      <div className="Upload">
        <span className="Title">Upload Files</span>
        <div className="Content">
          <div>
            <Dropzone
              onFilesAdded={this.onFilesAdded}
              disabled={this.state.uploading || this.state.successfullUploaded}
            />
          </div>
          <div className="Files">
            {this.state.files.map(file => {
              return (
                <div key={file.name} className="Row">
                  <span className="Filename">{file.name}</span>
                  {this.renderProgress(file)}
                </div>
              );
            })}
          </div>
        </div>
        <div className="Actions">{this.renderActions()}</div>
        
        {
          this.state.result ? 
          <MathDisplay 
            eqs={this.state.eq_list} 
            res={this.state.result} 
            handleCloseModal={this.handleCloseModal} 
            show={this.state.result ? true : false}
            deskewed_img={this.state.deskewed_img}
            cropped_img={this.state.cropped_img}
            original_img={this.state.original_img}

            
          ></MathDisplay>:null

        }
        
      </div>

    );
  }
}

export default Upload;
