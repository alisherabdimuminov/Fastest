from django import template
from quizzes.models import Result

register = template.Library()

@register.filter()
def status(quiz, user):
    result = Result.objects.filter(quiz=quiz, user=user)
    if result:
        result = result.first()
        if result.status == "passed":
            return "O'tgan"
        else:
            return "O'tmagan"
    return "Topshirilmagan"

@register.filter()
def result(quiz, user):
    result = Result.objects.filter(quiz=quiz, user=user)
    if result:
        return True
    return False

@register.simple_tag()
def res_id(quiz, user):
    return "result/" + str(Result.objects.filter(user=user, quiz=quiz).first().pk) + "/"


@register.filter()
def equal(answer, quiz):
    print(quiz)
    if answer == quiz.correct:
        return "correct"
    return answer + " " + quiz.correct
