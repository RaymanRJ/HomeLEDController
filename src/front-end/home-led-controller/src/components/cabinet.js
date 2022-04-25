import React, { Component } from 'react';
import { Box } from 'rebass';
import { Label, Select } from '@rebass/forms'
import { SwatchesPicker } from 'react-color';
import LEDStrip from './led_strip';

const API = process.env.REACT_APP_API_GATEWAY

export default class Cabinet extends Component {
    constructor(props){
        super(props)
        this.id = props.id
        this.led_strips = [
            <LEDStrip id="UPPER_LEFT" cabinet={this.id}/>,
            <LEDStrip id="UPPER_RIGHT" cabinet={this.id}/>,
            <LEDStrip id="LOWER_LEFT" cabinet={this.id}/>,
            <LEDStrip id="LOWER_RIGHT" cabinet={this.id}/>
        ]
    }

    componentDidMount = () => {
        var api = `${API}cabinetStatus/${this.id}`
        fetch(api)
            .then((response) => response.json())
            .then((json) => this.setState(json))
    }

    changeLEDStrip = (strip_id) => {
        this.setState(
            { cabinet: this.state.cabinet, strip_id: strip_id, background: this.state.background },
            () => this.handleChangeComplete()
        )
    }

    changeColor = (color) => {
        this.setState(
            { cabinet: this.state.cabinet, strip_id: this.state.strip_id, background: color.rgb },
            () => this.handleChangeComplete()
        )
    }

    handleChangeComplete = () => {
        var api = `${API}updateCabinet`
        fetch(api, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(this.state)
        })
    };

    create_form(){
        return(
            <div px={2}>
            <Box width={1} px={2}>
                <Label htmlFor='colour'>Colour:</Label>
                <SwatchesPicker 
                    color={ this.state?.background }
                    onChangeComplete={ (e) => this.changeColor(e) }
                />
            </Box>
            <Box width={1} px={2}>
                <Label htmlFor='ledstrip'>LED Strip:</Label>
                <Select
                    id='ledstrip'
                    name='ledstrip'
                    defaultValue='ALL'
                    onChange={ (e) => this.changeLEDStrip(e.target.value) }>
                    <option>ALL</option>
                    {this.led_strips.map((strip) => { return(<option>{strip.props.id}</option>) })}
                </Select>
            </Box>
            </div>
        )
    }

    format_string(string){
        return string.replace("_", " ")
    }

    render (){
        return(
            <div>
                Cabinet: {this.format_string(this.id)}
                {this.create_form()}
            </div>
        )
    }
}