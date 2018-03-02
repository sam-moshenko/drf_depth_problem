from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('body', 'pk')


class AnswerSerializer(WritableNestedModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ('question', 'body',)
