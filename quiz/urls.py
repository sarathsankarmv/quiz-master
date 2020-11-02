'''
Created on 2 Nov. 2020

@author: Sarath Sankar
'''

from django.contrib import admin
from django.urls import path
from quiz import views


urlpatterns = [
    path('', views.LoginView.as_view(), name='AdminLogin'),
    path('logout/', views.AdminLogout.as_view(), name='logout'),
    path('quiz/', views.QuizView.as_view(), name='quiz-view'),
    path('quiz/result/', views.ResultView.as_view(), name='result-view'),
    path('admin/', admin.site.urls),
]
