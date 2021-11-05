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
@api_view(['POST'])
def addExam(request):
    serializer = ExamSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"isSuccessful":True, "message": "Data saved successfully"})
    else:
       return Response({"isSuccessful":True, "message": "Data saved successfully"}) 
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
