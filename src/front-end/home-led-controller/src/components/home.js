import React, { Component } from 'react';
import { Tiles } from '@rebass/layout'
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
            <Tiles columns={[2, null, 4]}>
                {this.cabinets.map((cabinet) => {
                    return(
                        <div>
                            {cabinet}
                        </div>
                    )
                })}
            </Tiles>
        )
    }
}