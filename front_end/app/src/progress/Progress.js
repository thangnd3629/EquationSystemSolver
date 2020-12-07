import React, { Component } from "react";
import ProgressBar from 'react-bootstrap/ProgressBar'
import './Progress.css'

const Progress = ({done}) => {
	
	
	const newStyle = {
    opacity: 1,
    width: `${done}%`
  }
	
	return (
		<div className="progress">
			<div className="progress-done" style={newStyle}>
				{done}%
			</div>
		</div>
	)
}


export default Progress;
