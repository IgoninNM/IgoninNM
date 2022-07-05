from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name="news"),
    path('management', views.management, name='management'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('branches/', views.branches, name='all_branches'),
    path('branches/<str:country_name>', views.branches, name='branches'),
    path('cities/', views.cities, name="cities")
]


