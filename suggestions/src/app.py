import sys
import os

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
suggestions_grpc_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, suggestions_grpc_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc
from concurrent import futures

class SuggestionsService(suggestions_grpc.SuggestionsServicer):
    # TODO implement this logic
    def SuggestBooks(self, request, context):
        response = suggestions.SuggestionsResponse()
        
        item = response.suggestions.add()
        item.bookId = 1
        item.title = "The Hitchhiker's Guide to the Galaxy"
        item.author = "Douglas Adams"

        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    suggestions_grpc.add_SuggestionsServicer_to_server(SuggestionsService(), server)
    port = "50053"
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Listening on port 50053.")

    server.wait_for_termination()

if __name__ == '__main__':
    serve()