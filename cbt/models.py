from django.db import models


# Create your models here.
class Exam(models.Model):
    name = models.TextField()
    instruction = models.TextField()
    duration = models.IntegerField()

class Question(models.Model):
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()
    answerPosition: models.IntegerField

class Options(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionPosition = models.IntegerField()
    option: models.TextField()