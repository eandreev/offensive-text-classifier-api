import pickle
from classifier import ClassifyMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

class MessageClassifier(APIView):
    """
    Load the model at worker startup
    """
    with open('/opt/model.pickle', 'rb') as f:
        model = pickle.load(f)

    """
    Accept JSON POST payloads
    """
    parser_classes = (JSONParser,)
    
    def post(self, request):
        if 'text' not in request.data or str != type(request.data['text']):
            raise ParseError('The "text" string field is required')
        
        return Response({
            'class': int(self.model.classify(request.data['text']))
        })
