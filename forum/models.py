from django.db import models


class Accuracy(models.Model):
    percentage = models.CharField(max_length=4)


class Question(models.Model):
    body = models.TextField(max_length=1024)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField(max_length=1024)
    accuracy = models.ForeignKey(Accuracy, on_delete=models.CASCADE)