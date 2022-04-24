from flask import Flask, Response, make_response, jsonify, request, json
from flask_cors import CORS

from states.StateManager import StateManager

app = Flask(__name__)
CORS(app)

state_manager = StateManager()


@app.route('/cabinetStatus/<cabinetId>', methods=['GET'])
def cabinet_status(cabinetId: str):
    response = make_response(jsonify(
        {
            "cabinet": cabinetId,
            "strip_id": "ALL",
            "background": {
                "r": 183,
                "g": 28,
                "b": 28
            }
        }
    ), 200)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Credential', 'true')
    return response


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
