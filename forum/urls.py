from django.conf.urls import *
from .views import *

urlpatterns = [
    url(r'^question$', QuestionList.as_view()),
    url(r'^answer$', AnswerList.as_view()),
]
