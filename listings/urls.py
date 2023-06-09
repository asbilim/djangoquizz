from django.urls import path
from .views import single_quiz,quiz_done,quiz_error,explore

urlpatterns = [
    path('single/<int:quiz_id>/<int:question_id>',single_quiz,name="single-quiz"),
    path('done/<int:score>',quiz_done,name="done"),
    path('error',quiz_error,name="error"),
    path('explore',explore,name="explore"),
]
