from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Бұл жолды қосыңыз

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todo.urls')),
    path('', lambda request: redirect('todos/')),  # Автоматты бағыттау
]
