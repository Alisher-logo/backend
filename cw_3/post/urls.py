from django.urls import path
from .views import *

urlpatterns = [
    path('', lambda request: redirect('/threads/')),  # / → /threads
    path('threads/', thread_list, name='thread_list'),  # Тред тізімі
    path('threads/<int:id>/', thread_detail, name='thread_detail'),  # Тред және посттар
    path('threads/<int:id>/delete/', thread_delete, name='thread_delete'),  # Тред жою
    path('threads/<int:id>/edit/', thread_edit, name='thread_edit'),  # Тред өңдеу
    path('posts/<int:id>/delete/', post_delete, name='post_delete'),  # Пост жою
    path('posts/<int:id>/edit/', post_edit, name='post_edit'),  # Пост өңдеу
]
