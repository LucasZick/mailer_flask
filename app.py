from flask import Flask, request
from src.controllers.email import EmailController
from src import config

app = Flask(__name__)

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