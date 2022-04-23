import React, { Component } from 'react';
import { Box, Flex } from 'rebass';
import { Label, Select } from '@rebass/forms'
import { SwatchesPicker } from 'react-color';
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

        this.state = {
            cabinet: this.id,
            strip_id: "ALL",
            background: {
                r: 0,
                g: 0,
                b: 0
            }
        }
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
        console.log(this.state)
        // TODO: Send new state to backend
    };

    create_form(){
        return(
            <Box
            as='form'
            onSubmit={e => e.preventDefault()}
            py={3}>
            <Flex mx={-2} mb={3}>
                <Box width={1/2} px={2}>
                    <Label htmlFor='ledstrip'>LED Strip</Label>
                    <Select
                        id='ledstrip'
                        name='ledstrip'
                        defaultValue='ALL'
                        onChange={ (e) => this.changeLEDStrip(e.target.value) }>
                        <option>ALL</option>
                        {this.led_strips.map((strip) => { return(<option>{strip.props.id}</option>) })}
                    </Select>
                </Box>
                <Box width={1/2} px={2}>
                    <Label htmlFor='colour'>COLOUR</Label>
                    <SwatchesPicker onChangeComplete={ (e) => this.changeColor(e) } />
                </Box>
            </Flex>
        </Box>
        )
    }

    render (){
        return(
            <div>
                {this.id}
                {this.create_form()}
            </div>
        )
    }
}