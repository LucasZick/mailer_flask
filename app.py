from flask import Flask, request
from flask_cors import CORS
from src.controllers.email import EmailController
from src import config
from utils.is_alive_text import is_alive_text

app = Flask(__name__)
CORS(app, resources={"/sendEmail": {"origins": "https://zick.is-a.dev"},"/isAlive": {"origins": "*"}})

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
    if request.method == 'POST':
        if config.DEBUG:
            print(f'Message received from {request.remote_addr}')
        data = request.get_json()
        EmailController.send_message(data)
        return data
    
@app.route('/isAlive', methods=['GET'])
def isAlive():
    if request.method == 'GET':
        if config.DEBUG:
            print(f'Message received from {request.remote_addr}')
        return is_alive_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)