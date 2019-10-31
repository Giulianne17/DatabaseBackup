from django.conf.urls import url
from SystemsApp import views
from rest_framework import routers
from . import views
from django.urls import path

urlpatterns = [
    path('', views.SystemsList.as_view()),
    path('systems/<int:pk>/', views.SystemsDetail.as_view()),
    path('copy_backup/', views.CopyServerList.as_view()),
    path('copy_backup/<int:pk>/', views.CopyServerDetail.as_view()),
]
