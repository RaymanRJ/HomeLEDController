import LED from './led';
import { getLEDStripColour } from '../utils/requests';

export default class LEDStrip {

    constructor(id, cabinet){
        this.id = id
        this.cabinet = cabinet
        this.LEDs = []
        for(var i = 0; i < 16; i++)
            this.LEDs.push(<LED id={i} />)
        
        this.Colour = getLEDStripColour(cabinet, id)
    }

    changeColour(colour){
        this.Colour = colour
    }
}