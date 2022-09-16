from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import Company_views
urlpatterns = [
    path("",Company_views.as_view()),
    path("<int:id>",Company_views.as_view())
]
