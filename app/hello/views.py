from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import *


# Create your views here.
def index(request):
    days = ["понедельник", "вторник", "среда", "четверг 010203", "пятница", "суббота", "воскресенье"]
    dye_of_week = days[datetime.today().weekday()]
    # template_object = loader.get_template('hello/index.html')
    # text = template_object.render({'my_variable'}: day_of_week})
    # return HttpResponse(text)
    return render(request, 'hello/index.html', {'my_variable': dye_of_week})


def news(request):
    return render(request, "hello/news.html")


def management(request):
    return render(request, "hello/management.html")


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def branches(request, country_name=""):
    if country_name == "":
        country_name = " всех городах"
    return render(request, 'hello/branches.html', {'country_name': country_name})


def page_not_found(request, exception=None):
    response = render(request, 'hello/404.html')
    response.status_code = 404
    return response


def cities(request):
    query_set = City.objects.all()
    return render(request, "hello/cities.html", {"cities": query_set})
