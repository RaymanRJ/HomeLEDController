import React, { Component, useState } from 'react';
import { Box, Flex } from 'rebass';
import { Label, Select } from '@rebass/forms'
import { SwatchesPicker } from 'react-color';
import LEDStrip from './led_strip';
import getInitCabinet from '../utils/requests'
const API = process.env.REACT_APP_API_GATEWAY

export default class Cabinet extends Component {
    constructor(props){
        super(props)
        console.log('Cabinet Constructor')
        this.id = props.id
        this.led_strips = [
            <LEDStrip id="UPPER_LEFT" cabinet={this.id}/>,
            <LEDStrip id="UPPER_RIGHT" cabinet={this.id}/>,
            <LEDStrip id="LOWER_LEFT" cabinet={this.id}/>,
            <LEDStrip id="LOWER_RIGHT" cabinet={this.id}/>
        ]
    }

    componentDidMount = () => {
        console.log('Cabinet Mounted')
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
        console.log(this.state)
        // TODO: Send new state to backend
    };

    create_form(){
        console.log('Cabinet Form created')
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
                    <SwatchesPicker 
                        color={ this.state?.background }
                        onChangeComplete={ (e) => this.changeColor(e) }
                    />
                    
                </Box>
            </Flex>
        </Box>
        )
    }

    render (){
        console.log('Cabinet render')
        return(
            <div>
                {this.id}
                {this.create_form()}
            </div>
        )
    }
}