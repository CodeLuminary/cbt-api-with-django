from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
@api_view(['GET'])
def getUsers(request):
    pass
def addUser(request):
    pass
def addExam(request):
    pass
def getExams(request):
    pass
def getExam(request):
    pass
def addExamQuestion(request):
    pass
def getExamQuestions(request):
    pass
def userLogin(request):
    return render(request,'login.html')
    pass
def login(request):
    pass
