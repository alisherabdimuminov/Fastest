from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import (
    Set,
    Question,
    Quiz,
    Result,
)


@admin.register(Result)
class ResultModelAdmin(ModelAdmin):
    list_display = ["user", "quiz", "correct", "score", "status"]
    readonly_fields = ["user", "quiz", "correct", "score", "status", "questions", "answers"]
    list_filter = ["user", "quiz"]


class QuestionInline(admin.TabularInline):
    model = Question
    fields = ["body", "answer_a", "answer_b", "answer_c", "answer_d"]
    extra = 1

@admin.register(Question)
class QuestionModelAdmin(ModelAdmin):
    list_display = ["body", ]


@admin.register(Set)
class SetModelAdmin(ModelAdmin):
    inlines = [QuestionInline, ]
    list_display = ["name", "count_questions"]


@admin.register(Quiz)
class QuizModelAdmin(ModelAdmin):
    list_display = ["name", "number"]
