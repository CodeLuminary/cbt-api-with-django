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

class Users(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    isEnabled = models.BooleanField()
