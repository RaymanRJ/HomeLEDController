import React, { Component } from 'react';
import { Flex } from 'rebass';
import Cabinet from './cabinet';

export default class Home extends Component {
    constructor(props){
        super(props)

        this.cabinets=[
            <Cabinet id="OUTER_LEFT"/>,
            <Cabinet id="INNER_LEFT"/>,
            <Cabinet id="INNER_RIGHT"/>,
            <Cabinet id="OUTER_RIGHT"/>
        ]
    }
    
    render (){
        return(
            <Flex mx={-2}>
                {
                    this.cabinets.map((cabinet) => {
                        return(
                            <div key={cabinet}>
                                {cabinet}
                            </div>
                        )
                    })
                }
            </Flex>
        )
    }
}