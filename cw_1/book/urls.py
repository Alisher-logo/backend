from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),               # 📚 Басты бет ретінде кітаптар тізімі
    path('books/', views.book_list, name='book_list'),         # Кітаптар тізімі
    path('books/<int:id>/', views.book_detail, name='book_detail'),  # Жеке кітап мәліметі
]
