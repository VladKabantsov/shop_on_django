from django.shortcuts import render
from news.models import *


def news(request, news_id):
    news = News.objects.get(id=news_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())