from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from quiz.models import *
# Create your views here.

def Quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            correct_choice_id = question.choice_set.filter(is_correct=True).first().id
            if selected_choice_id == str(correct_choice_id):
                score += 5

        messages.success(request, f'Your score is {score}/{Question.objects.count()}')
        return HttpResponse(str(score))

    return render(request, 'Quiz.html', {'questions': questions})


def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            correct_choice_id = question.choice_set.filter(is_correct=True).first().id
            if selected_choice_id == str(correct_choice_id):
                score += 1

        messages.success(request, f'Your score is {score}/{Question.objects.count()}')
        return redirect('quiz:quiz')

    return HttpResponse('Method Not Allowed', status=405)

