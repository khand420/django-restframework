from . import views, viewsCls, viewsGeneric

from django.contrib import admin
from django.urls import path,include
from .routers import router



urlpatterns = [
    path('', views.get_home, name = 'home'),
    path('post-todo/', views.post_todo, name = 'post-todo'),
    path('get-todo/', views.get_todo, name = 'get-todo'),
    path('patch-todo/', views.patch_todo, name = 'patch-todo'),

    path('todo/', viewsCls.TodoView.as_view(), name = 'patch-todo'),

    path('todo-generic/', viewsGeneric.TodoGen.as_view(), name = 'gen-todo'),
    path('todo-generic/<uid>/', viewsGeneric.TodoGenerci.as_view(), name = 'gen-todo2'),





]

urlpatterns+=router.urls  
