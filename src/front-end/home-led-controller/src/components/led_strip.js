import React, { Component } from 'react';
import LED from './led';

export default class LEDStrip extends Component {

    constructor(props){
        super(props)
        this.id = props.id
        this.LEDs = []
        for(var i = 0; i < 16; i++)
            this.LEDs.push(<LED id={i} />)
    }

    render (){
        return(
            <p>{this.id}</p>
        )
    }
}