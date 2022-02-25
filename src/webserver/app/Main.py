from flask import Flask, make_response, jsonify, request

from app.states.StateManager import StateManager

app = Flask(__name__)

state_manager = StateManager()


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
