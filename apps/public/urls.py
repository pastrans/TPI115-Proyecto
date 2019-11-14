from django.urls import path
from django.conf.urls import url
from apps.public.views import index

urlpatterns = [
    path('', index, name="myindex"),
]