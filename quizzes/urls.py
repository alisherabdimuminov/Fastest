from django.urls import path

from .views import (
    home,
    quiz_page,
    result,
)


urlpatterns = [
    path("", home, name="home"),
    path("quiz/<int:id>/", quiz_page, name="quiz"),
    path("result/<int:id>/", result, name="result"),
]