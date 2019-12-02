from django.urls import path
from django.conf.urls import url
from apps.public.views import index, Pdf

urlpatterns = [
    path('', index, name="myindex"),
    path('pdf', Pdf.as_view(), name="pdf")
    #path('pdf', some_view, name='pdf')
]