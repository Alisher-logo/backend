from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/todo-lists/')),  # Бастапқы бет
    path('todo-lists/', include('todos.urls')),
]
