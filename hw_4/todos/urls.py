from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name="todo_list"),
    path('<int:id>/', views.todo_list_detail, name="todo_list_detail"),
    path('<int:id>/edit/', views.todo_list_edit, name="todo_list_edit"),
    path('<int:id>/delete/', views.todo_list_delete, name="todo_list_delete"),
    path('todos/<int:todo_id>/edit/', views.todo_edit, name="todo_edit"),
    path('todos/<int:todo_id>/delete/', views.todo_delete, name="todo_delete"),
]
