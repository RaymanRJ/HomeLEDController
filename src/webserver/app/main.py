from flask import Flask, make_response, jsonify, request

from app.states.StateManager import StateManager

app = Flask(__name__)

state_manager = StateManager()


"""
Sample post data:
{
    'state_type': LED_STATE,
    'state_changes': {
        'cabinets': {
            'ALL': {
                'led_strips': {
                    'ALL': {
                        leds: {
                            'ALL':{
                                led_details:{
                                    r: int,
                                    g: int,
                                    b: int,
                                    brightness: int
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

OR:

{
    'state_type': LED_STATE,
    'state_changes': {
        'cabinets': {
            'OUTER_LEFT': {
                'led_strips: {
                    UPPER_RIGHT: {
                        leds: {
                            0: {
                                r: int,
                                b: int,
                                g: int,
                                brightness: int
                            },
                            14: {
                                r: int,
                                ...
                            }
                        }
                    }
                }
            }
        }
    }
}
"""
@app.route('/updateLEDs', methods=['POST'])
def update_LEDs():
    return make_response(
        jsonify(
            state_manager.update_state(request.get_json())
        )
    )


@app.route('/healthcheck')
def health_check():
    return make_response(
        jsonify({'status': 'healthy'}),
        200
    )


if __name__ == "__main__":
    app.run()

