from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import *


# Create your views here.
def index(request):
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    dye_of_week = days[datetime.today().weekday()]
    # template_object = loader.get_template('hello/index.html')
    # text = template_object.render({'my_variable'}: day_of_week})
    # return HttpResponse(text)
    return render(request, 'hello/index.html', {'day_of_week': dye_of_week})


def page_not_found(request, exception=None):
    response = render(request, 'hello/404.html')
    response.status_code = 404
    return response


def cities(request):
    if 'city' in request.GET and 'year' in request.GET:
        query_set = Event.objects.filter(city__slug=request.GET['city'], year__slug=request.GET['city'])
    else:
        query_set = City.objects.all()

    # if slug:
    #     query_set = City.objects.filter(slug=slug)
    # else:
    #     query_set = City.objects.all()

    return render(request, "hello/page.html", {
        "query_set": query_set,
        "name_of_page": "Города"
    })


def history(request):
    query_set = Year.objects.all()
    return render(request, "hello/page.html", {
        "query_set": query_set,
        "name_of_page": "История"
    })


def facts(request):
    query_set = Event.objects.all()
    return render(request, "hello/page.html", {
        "query_set": query_set,
        "name_of_page": "События"
    })


def article_city(request, place):
    event_place = City.objects.get(slug=place)
    events = Event.objects.filter(city=event_place.id)
    return render(request, "hello/detali_page.html", {
        "events": events
    })


def article_history(request, year):
    event_year = Year.objects.get(slug=year)
    events = Event.objects.filter(year=event_year.id)

    return render(request, "hello/detali_page.html", {
        "events": events
    })


def article_city_history(request, year, place):
    event_year = Year.objects.get(slug=year)
    event_place = City.objects.get(slug=place)
    events = Event.objects.filter(city=event_place.id, year=event_year.id)

    return render(request, "hello/detali_page.html", {
        "events": events
    })
