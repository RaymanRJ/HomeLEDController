from flask import Flask, make_response, jsonify, request

from states.StateManager import StateManager

app = Flask(__name__)

state_manager = StateManager()


@app.route('/cabinetStatus/<cabinet_id>', methods=['GET'])
def cabinet_status(cabinet_id: str):
    response_data = {
        "cabinet": cabinet_id,
        "strip_id": "ALL",
        "background": {
            "r": 48,
            "g": 63,
            "b": 159
        }
    }
    return jsonify(response_data), 200


@app.route('/updateCabinet/<cabinet_id>', methods=['POST'])
def update_cabinet(cabinet_id: str):
    data = request.get_json()
    print(data)
    return jsonify({'status': 'healthy'}), 200


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
