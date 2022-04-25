from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from states.StateManager import StateManager

app = Flask(__name__)
CORS(app, support_credentials=True)
state_manager = StateManager()


@app.route('/cabinetStatus/<cabinet_id>', methods=['GET'])
def cabinet_status(cabinet_id: str):
    response_data = jsonify(state_manager.get_cabinet_state(cabinet_id))
    response_data.access_control_allow_origin = '*'
    return response_data, 200


@app.route('/updateCabinet', methods=['POST'])
def update_cabinet():
    data = request.get_json()
    response_data = jsonify(state_manager.update_state(data))
    response_data.access_control_allow_origin = '*'
    return response_data, 200


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
    app.run(host='0.0.0.0')
