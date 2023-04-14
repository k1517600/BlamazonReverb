from flask import Flask, request, Response
from flask_cors import CORS
import time
import intenthandler

app = Flask(__name__)
CORS(app)


@app.route("/AlexWebhook", methods=['POST'])
def fulfill_request():
    payload = request.json
    function_name = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    print(function_name)
    intent_handler = getattr(intenthandler, function_name)
    response_text = intent_handler(parameters)
    print(payload)

    return {'fulfillmentText': response_text}


if __name__ == "__main__":
    app.run(debug=True)
