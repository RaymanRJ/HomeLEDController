import React, { Component } from 'react';
import { Box } from 'rebass';
import { Label, Select, Checkbox } from '@rebass/forms'
import { SwatchesPicker } from 'react-color';
import LEDStrip from './led_strip';

const API = process.env.REACT_APP_API_GATEWAY

export default class Cabinet extends Component {
    constructor(props){
        super(props)
        this.id = props.id
        this.led_strips = {
            "UPPER_LEFT": new LEDStrip("UPPER_LEFT", this.id),
            "UPPER_RIGHT": new LEDStrip("UPPER_RIGHT", this.id),
            "LOWER_LEFT": new LEDStrip("LOWER_LEFT", this.id),
            "LOWER_RIGHT": new LEDStrip("LOWER_RIGHT", this.id)
        }
        // this.led_strips = [
        //     new LEDStrip ("UPPER_LEFT", this.id),
        //     new LEDStrip ("UPPER_RIGHT", this.id),
        //     new LEDStrip ("LOWER_LEFT", this.id),
        //     new LEDStrip ("LOWER_RIGHT", this.id)
        // ]

        this.state = {
            background: '',
            selectDisabled: false,
            selectedLEDStrip: this.led_strips["UPPER_LEFT"],
            lastSelectedLEDStrip: this.led_strips["UPPER_LEFT"]
        }
    }

    componentDidMount = () => {
        this.setState(
            {
                selectDisabled: false,
                selectedLEDStrip: this.led_strips["UPPER_LEFT"],
                background: this.getBackground()
            }
        )
    }

    changeLEDStrip = (strip_id) => {
        this.setState(
            {
                ...this.state,
                lastSelectedLEDStrip: this.state.selectedLEDStrip,
                selectedLEDStrip: this.led_strips[strip_id],
            }, () => this.handleChangeComplete()
        )
    }

    changeColour = (colour) => {
        if (this.state.selectDisabled)
            this.setState({
                ...this.state,
                background: colour
            },
            () => this.handleChangeComplete())
        else{
            this.state.selectedLEDStrip.changeColour(colour)
            this.setState({
                ...this.state,
                background: colour
            }, () => this.handleChangeComplete())
        }
    }

    changeAllBtn = (checked) => {
        this.setState(
            { 
                ...this.state,
                selectDisabled: checked,
                lastSelectedLEDStrip: this.state.selectedLEDStrip,
                selectedLEDStrip: checked ? 'ALL' : this.state.lastSelectedLEDStrip
             },
             () => this.handleChangeComplete()
        )
    }

    getBackground(){
        return this.state.selectedLEDStrip.Colour ?? "000"
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
            body: JSON.stringify({
                ...this.state,
                cabinet_id: this.id
            })
        })
    };

    create_form(){
        return(
            <div px={2}>
            <Box width={1} px={2}>
                <Label htmlFor='colour'>Colour:</Label>
                { 
                    this.state ? 
                        <SwatchesPicker 
                            color={ this.state.background }
                            onChangeComplete={ (e) => this.changeColour(e) }
                        />
                    : null 
                }
            </Box>
            <Box width={1} px={2}>
                <Box width={3/4} px={2}>
                    <Label htmlFor='ledstrip'>LED Strip:</Label>
                    <Select
                        id='ledstrip'
                        name='ledstrip'
                        onChange={ (e) => this.changeLEDStrip(e.target.value) }
                        disabled={ this.state?.selectDisabled }>
                        {
                            Object.keys(this.led_strips).map((key) => {
                                return(<option>{key}</option>) 
                            })
                        }
                        {/* {this.led_strips.kmap((strip) => { return(<option>{strip.id}</option>) })} */}
                    </Select>
                </Box>
                <Box width={1/4} px={2}>
                    <Label>
                        <Checkbox id='allbtn' name='allbtn' onChange={ (e) => this.changeAllBtn(e.target.checked)}/>
                        All
                    </Label>
                </Box>
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