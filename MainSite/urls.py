"""MainSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Handicapskydning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Index.as_view()),
    path("klubber/", views.Clubs.as_view()),
    path("galleri/", views.Gallery.as_view()),
    path("kalender/", views.Kalender.as_view()),
    path("baner/", views.Lanes.as_view()),
    path("links/", views.Links.as_view()),
    path("nyheder/", views.News.as_view()),
    path("andre/", views.Other.as_view()),
    path("resultater/", views.Results.as_view()),
    path("regler/", views.Rules.as_view()),
    path("bestyrelse/", views.Staff.as_view()),
    path("bestyrelse/<int:pk>/", views.StaffDetail.as_view()),
]
