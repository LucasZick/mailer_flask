from flask import Flask, request
from flask_cors import CORS
from src.controllers.email import EmailController
from src import config

app = Flask(__name__)
CORS(app)#, resources={r"/sendEmail": {"origins": config.ALLOWED_CORS}})

@app.route('/sendEmail', methods=['POST'])
def hello():
    if request.method == 'POST':
        if config.DEBUG:
            print(f'Message received from {request.remote_addr}')
        data = request.get_json()
        EmailController.send_message(data)
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=config.DEBUG)