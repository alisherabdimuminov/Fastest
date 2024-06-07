from django.urls import path

from .views import (
    home,
    quiz_page,
)


urlpatterns = [
    path("", home, name="home"),
    path("quiz/<int:id>/", quiz_page, name="quiz"),
]