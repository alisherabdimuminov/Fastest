from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User


def default():
    return {}

STATUS = (
    ("passed", "O'tgan"),
    ("failed", "O'tmagan"),
)


class Set(models.Model):
    name = models.CharField(max_length=100, verbose_name="To'plam nomi")

    def __str__(self):
        return self.name
    
    def questions(self):
        return Question.objects.filter(set=self)
    
    def count_questions(self):
        return Question.objects.filter(set=self).count()
    
    class Meta:
        verbose_name = "To'plam"
        verbose_name_plural = "To'plamlar"
    

class Question(models.Model):
    body = models.TextField(verbose_name="Savol")
    set = models.ForeignKey(Set, on_delete=models.CASCADE, verbose_name="To'plam")
    answer_a = models.TextField(verbose_name="A varyant (To'g'ri javob)")
    answer_b = models.TextField(verbose_name="B varyant")
    answer_c = models.TextField(verbose_name="C varyant")
    answer_d = models.TextField(verbose_name="D varyant")
    correct = models.TextField(verbose_name="To'g'ri javob (a, b, c, d)")

    def __str__(self):
        return self.body
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class Quiz(models.Model):
    name = models.CharField(max_length=100, verbose_name="Test nomi")
    set = models.ForeignKey(Set, on_delete=models.CASCADE, verbose_name="Test uchun savollar to'plami")
    passing_score = models.IntegerField(validators=[MaxValueValidator(limit_value=100, message="Mksimal qiymat 100"), MinValueValidator(limit_value=50, message="Minimal qiymat 50")], verbose_name="O'tish bali")
    number = models.IntegerField(verbose_name="Test savollar soni", validators=[MaxValueValidator(limit_value=100, message="Maksimal savollar soni 100"), MinValueValidator(limit_value=10, message="Minimal savollar soni 10")])
    submitters = models.ManyToManyField(User, related_name="quiz_submitters", verbose_name="Testni topshiradiganlar", null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Test")
    correct = models.IntegerField(editable=False, verbose_name="To'g'ri javoblar soni")
    score = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Ball")
    questions = models.ManyToManyField(Question, related_name="result_questions", null=True, blank=True, verbose_name="Savollar")
    answers = models.JSONField(default=default)
    status = models.CharField(max_length=100, verbose_name="Holati", choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"

