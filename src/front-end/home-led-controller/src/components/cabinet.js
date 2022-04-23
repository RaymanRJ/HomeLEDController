import React, { Component } from 'react';
import LEDStrip from './led_strip';

export default class Cabinet extends Component {
    constructor(props){
        super(props)
        this.id = props.id
        this.led_strips = [
            <LEDStrip id="UPPER_LEFT"/>,
            <LEDStrip id="UPPER_RIGHT"/>,
            <LEDStrip id="LOWER_LEFT"/>,
            <LEDStrip id="LOWER_RIGHT"/>
        ]
    }

    render (){
        return(
            <div>
                {this.id}
                <ul>
                    {this.led_strips.map((strip) => {
                        return(<li>{strip.props.id}</li>)
                    })}
                </ul>
            </div>
        )
    }
}