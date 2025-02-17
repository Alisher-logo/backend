from django.http import JsonResponse
from .models import Article
from django.shortcuts import render

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
        return JsonResponse({
            'title': article.title,
            'text': article.text,
            'author': article.author
        })
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)
