from rest_framework.generics import *
from .serializers import *


# Create your views here.
class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
