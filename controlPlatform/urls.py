from django.urls import path, include

from controlPlatform import views

urlpatterns = [
    path('', views.controlPlatform),
    path('get_by_id', views.MarkingDataOperation.get_by_id)
]