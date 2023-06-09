from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class QuizCategories(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Answer(models.Model):

    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer + " correct" if self.is_correct else self.answer + " not correct"
    
class Question(models.Model):

    name = models.CharField(max_length=3000)
    has_multiple_answers = models.BooleanField(default=False)
    category = models.ForeignKey(QuizCategories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField(Answer,null=True,blank=True)

    def __str__(self):
        return self.name




class Quiz(models.Model):

    name = models.CharField(max_length=50)
    question_time = models.IntegerField(default=60) #this will serve to determine when to stop the quizz
    questions = models.ManyToManyField(Question)
    question_value = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Exam(models.Model):

    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField()
    has_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " did " + self.quiz.name
