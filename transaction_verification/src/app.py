import sys
import os

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
transaction_verification_grpc_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, transaction_verification_grpc_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc
from concurrent import futures

class TransactionVerificationService(transaction_verification_grpc.TransactionVerificationServicer):
    # TODO implement this logic
    def VerifyTransaction(self, request, context):
        response = transaction_verification.VerifyTransactionResponse()
        response.is_verified = True

        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    transaction_verification_grpc.add_TransactionVerificationServicer_to_server(TransactionVerificationService(), server)
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Listening on port 50052.")

    server.wait_for_termination()

if __name__ == '__main__':
    serve()