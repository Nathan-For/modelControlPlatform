from django.urls import path, include

from carefulTraining import views

urlpatterns = [
    path('', views.carefulTraining),
]