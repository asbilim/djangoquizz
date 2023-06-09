from django.urls import path
from .views import single_quiz

urlpatterns = [
    path('single/<int:quiz_id>/<int:question_id>',single_quiz,name="single-quiz")
]
