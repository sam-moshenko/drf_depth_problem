from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('body', 'pk')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'body',)
        depth = 1  # this causes 'create' method to ignore question, comment to make it work, but without depth
