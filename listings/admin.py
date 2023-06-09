from django.contrib import admin
from . models import Answer,Exam,Question,Quiz,QuizCategories

admin.site.register(Answer)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizCategories)
