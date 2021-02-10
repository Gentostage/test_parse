from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostlView.as_view()),

]
