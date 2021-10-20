from django.urls import path
from . import views

urlpatterns = [
    path('/api/get-users', views.getUsers),
    path('/api/add-users', views.addUser),
    path('/api/add-exams', views.addExam),
    path('/api/get-exams', views.getExams),
    path('/api/get-exam', views.getExam),
    path('/api/add-exam-questions', views.addExamQuestion),
    path('/api/get-exam-questions', views.getExamQuestions),
    path('/account/login',views.userLogin),
    path('/api/login-users', views.login),
]
