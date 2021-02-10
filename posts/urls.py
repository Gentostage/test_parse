from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostDetailView.as_view()),

]
