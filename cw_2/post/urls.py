from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),                # GET /posts/
    path('<int:id>/', views.post_detail, name='post_detail'),   # GET /posts/:id
    path('create/', views.post_create, name='post_create'),     # POST /posts/
    path('<int:id>/delete/', views.post_delete, name='post_delete'),  # DELETE /posts/:id/delete
]
