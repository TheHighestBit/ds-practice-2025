import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
grpc_paths = ['fraud_detection', 'transaction_verification', 'suggestions']
for grpc_path in grpc_paths:
    grpc_path = os.path.abspath(os.path.join(FILE, f'../../../utils/pb/{grpc_path}'))
    sys.path.insert(0, grpc_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc

def check_for_fraud(request_json):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = fraud_detection_grpc.FraudDetectionStub(channel)
        req = fraud_detection.FraudDetectionRequest()

        req.user.name = request_json['user']['name']
        req.user.contact = request_json['user']['contact']

        req.credit_card.card_number = request_json['creditCard']['number']
        req.credit_card.expiration_date = request_json['creditCard']['expirationDate']
        req.credit_card.cvv = request_json['creditCard']['cvv']

        req.billing_address.street = request_json['billingAddress']['street']
        req.billing_address.city = request_json['billingAddress']['city']
        req.billing_address.state = request_json['billingAddress']['state']
        req.billing_address.zip = request_json['billingAddress']['zip']
        req.billing_address.country = request_json['billingAddress']['country']

        response = stub.DetectFraud(req)

        if response.is_fraudulent == True:
            return True, response.reason
        else:
            return False, "No fraud detected."

def verify_transaction(request_json):
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionVerificationStub(channel)
        req = transaction_verification.VerifyTransactionRequest(
            gift_wrapping=False, terms_accepted=True)

        req.user.name = request_json['user']['name']
        req.user.contact = request_json['user']['contact']

        req.credit_card.card_number = request_json['creditCard']['number']
        req.credit_card.expiration_date = request_json['creditCard']['expirationDate']
        req.credit_card.cvv = request_json['creditCard']['cvv']

        req.billing_address.street = request_json['billingAddress']['street']
        req.billing_address.city = request_json['billingAddress']['city']
        req.billing_address.state = request_json['billingAddress']['state']
        req.billing_address.zip = request_json['billingAddress']['zip']
        req.billing_address.country = request_json['billingAddress']['country']
        
        for item in request_json['items']:
            item_obj = req.items.add()
            item_obj.name = item['name']
            item_obj.quantity = item['quantity']

        response = stub.VerifyTransaction(req)

        if response.is_verified == True:
            return True
        else:
            return False
        
def get_suggestions(request_json):
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = suggestions_grpc.SuggestionsStub(channel)
        req = suggestions.SuggestionsRequest()

        item1 = req.items.add()
        item1.name = "Some fantastic book"
        item1.quantity = 1

        item2 = req.items.add()
        item2.name = "Some other fantastic book"
        item2.quantity = 1

        response = stub.SuggestBooks(req)

        return response.suggestions

# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request
from flask_cors import CORS
import json

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app, resources={r'/*': {'origins': '*'}})

# Define a GET endpoint.
@app.route('/', methods=['GET'])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    response = greet(name='orchestrator')
    # Return the response.
    return response

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    # Get request object data to json
    request_data = json.loads(request.data)
    # Print request object data
    print("Request Data:", request_data)

    print("fraud detection result", check_for_fraud(request_data))
    print("verification result", verify_transaction(request_data))
    print("Suggested books:", get_suggestions(request_data))

    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': '12345',
        'status': 'Order Approved',
        'suggestedBooks': [
            {'bookId': '123', 'title': 'The Best Book', 'author': 'Author 1'},
            {'bookId': '456', 'title': 'The Second Best Book', 'author': 'Author 2'}
        ]
    }

    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
