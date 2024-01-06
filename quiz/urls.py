# quiz/urls.py
from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('Quiz/', Quiz, name='Quiz'),
    path('submit_quiz/', submit_quiz, name='submit_quiz'),
]
