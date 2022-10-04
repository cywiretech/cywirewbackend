from django.urls import path
from . import views


# API EPlanet Mobile

urlpatterns = [
    path('getNewsletter/', views.getNewsletter),
    path('addNewsletter/', views.addNewsletter)
]
