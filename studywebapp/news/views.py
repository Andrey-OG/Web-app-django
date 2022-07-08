from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by("date")
    data = {
        "title": "Новости",
        "news": news,
    }
    return render(request, "news/news_home.html", data)


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Форма была заполнена некорректно"

    data = {
        "title": "Создание новости",
        "form": ArticlesForm(),
        "error": error,
    }
    return render(request, "news/create.html", data)


# Create your views here.
