from rest_framework import serializers
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer

class AccuracySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accuracy
        fields = "__all__"

class AnswerSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Answer
        fields = ("__all__")
        depth = 1


class QuestionSerializer(WritableNestedModelSerializer):
    answer_set = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('body', 'pk', "answer_set")