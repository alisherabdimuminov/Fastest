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
