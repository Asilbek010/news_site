

from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from news_app.models import News

def news_list_view(request):
    news_list = News.published.all()
    xorij_news = News.published.filter(category__name = 'Xorij')[:5]
    mahalliy_news = News.published.filter(category__name = 'Mahalliy')[:5]
    sport_news = News.published.filter(category__name = 'Sport')[:5]
    texnology_news = News.published.filter(category__name = 'Texnologiya')[:5]
    context = {
        'news_list': news_list,
        'xorij_news': xorij_news,
        'mahalliy_news': mahalliy_news,
        'sport_news': sport_news,
        'texnology_news': texnology_news

    }
    return render(request, 'index.html', context)

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'


def new_detail_view(request, slug):
    news = News.objects.get(slug=slug)
    three_news = News.published.filter(category__name = news.category).exclude(id=news.id)[:3]
    context = {
        'news': news,
        'three_news': three_news,
    }

    return render(request, 'single_page.html', context)

def contact_view(request):
    return render(request, template_name='contact.html')

def local_news_view(request):
    news_list = News.published.filter(category__name = 'Mahalliy')

    context = {'news_list': news_list}

    return render(request, 'local_news.html', context)



