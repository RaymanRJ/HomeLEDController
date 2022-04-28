import React, { Component } from 'react';
import LED from './led';

const API = process.env.REACT_APP_API_GATEWAY

export default class LEDStrip {

    constructor(id, cabinet){
        this.id = id
        this.cabinet = cabinet
        this.Colour = null
        this.LEDs = []
        for(var i = 0; i < 16; i++)
            this.LEDs.push(<LED id={i} />)
        
        this.setup()
    }

    changeColour(colour){
        this.Colour = colour
    }

    setup(){
        var api = `${API}ledStatus?cabinet=${this.cabinet}&strip=${this.id}`
        fetch(api)
            .then((response) => response.json())
            .then((json) => {
                this.Colour = json['background']
            })
    }
}