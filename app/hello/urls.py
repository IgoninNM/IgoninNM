from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('cities/', views.cities, name="cities"),

    path('cities/<slug:place>/', views.article_city, name="article_city"),
    path('history/<int:year>/', views.article_history, name="article_history"),
    path('cities/<slug:place>/<int:year>/', views.article_city_history, name="article_city_history"),

    path('history/', views.history, name="history"),
    path('facts/', views.facts, name="facts")
]


