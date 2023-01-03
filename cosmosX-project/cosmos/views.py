from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'cosmos/html/index.html')


def news(request):
    all_news = News.objects.all()
    paginator = Paginator(all_news, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cosmos/html/news.html', {'page_obj': page_obj, 'all_news': all_news})


def team(request):
    return render(request, 'cosmos/html/team.html')


def gallery(request):
    return render(request, 'cosmos/html/team.html')


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'cosmos/html/detail.html', {'news': news})
