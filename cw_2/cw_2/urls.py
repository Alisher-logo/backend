from django.contrib import admin
from django.urls import path, include
from post import views  # post қосымшасынан views импорттау

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),   # Басты бетке барлық посттарды көрсету
    path('posts/', include('post.urls')),
]
