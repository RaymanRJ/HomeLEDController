import React, { Component } from 'react';

export default class LED extends Component {

    constructor(props){
        super(props)
        this.id = props.id
        this.red = 0
        this.green = 0
        this.blue = 0
        this.brightness = 0
    }

    render (){
        return(
            <p>{this.id}</p>
        )
    }
}