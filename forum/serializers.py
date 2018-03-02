from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('body', 'pk')


class AnswerSerializer(serializers.ModelSerializer):
    question_pk = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(), source='question', write_only=True
    )

    class Meta:
        model = Answer
        fields = ('question', 'question_pk', 'body',)
        depth = 1

