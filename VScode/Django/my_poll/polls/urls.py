# 2차 url
from django.urls import path
# from .views import *
from . import views

urlpatterns = [
    # path("list/", list),
    path("list/", views.list, name='list'),
    path("vote_form/<int:question_id>", views.vote_form, name='vote_form'),
]