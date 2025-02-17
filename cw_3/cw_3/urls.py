from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_threads(request):
    return redirect('thread_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_threads),  # Басты бетті /threads-ке бағыттау
    path('threads/', include('post.urls')),
]
