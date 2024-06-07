import random
from django.http import HttpRequest
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    User,
    Question,
    Quiz,
    Set,
    Result
)


@login_required(login_url="login")
def home(request: HttpRequest):
    context = {}
    user = request.user
    quizzes = Quiz.objects.filter(submitters=user)
    context["quizzes"] = quizzes
    return render(
        request=request,
        template_name="home.html",
        context=context
    )

@login_required(login_url="login")
def quiz_page(request: HttpRequest, id: int):
    context = {}
    quiz = get_object_or_404(Quiz, pk=id)
    user = request.user
    d = {}
    correct = 0
    score = 0
    status = None
    if user not in quiz.submitters.all():
        return redirect("home")
    result = Result.objects.filter(user=user, quiz=quiz)
    if result:
        return redirect("home")
    questions = Question.objects.filter(set=quiz.set).order_by("?")[:quiz.number]
    if request.method == "POST":
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        for qi, qj in zip(questions, data):
            print(qi.correct, data[qj])
            if qi.correct == data[qj]:
                d[qj] = "correct"
                correct += 1
            else:
                d[qj] = "incorrect"
        score = (correct / quiz.number) * 100
        if score >= quiz.passing_score:
            status = "passed"
        else:
            status = "failed"
        r = Result.objects.create(
            user=user,
            quiz=quiz,
            correct=correct,
            score=score,
            status=status,
            answers=d
        )
        r.questions.set(questions)
        r.save()
        return redirect("home")
    context["quiz"] = quiz
    context["questions"] = questions
    return render(
        request=request,
        template_name="quiz.html",
        context=context
    )
