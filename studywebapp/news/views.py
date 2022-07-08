from django.shortcuts import render
from .models import Articles


def news_home(request):
    news = Articles.objects.order_by("date")
    data = {
        "title": "Новости",
        "news": news,
    }
    return render(request, "news/news_home.html", data)


# Create your views here.
