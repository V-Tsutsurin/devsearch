from django.shortcuts import render, get_object_or_404
from .models import News


def news(request):
    news_list = News.objects.order_by('-date')
    return render(request, 'news/news.html', {'news_list': news_list})


def detail(request, news_id):
    single_news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_page.html', {"news": single_news})
