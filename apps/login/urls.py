from django.urls import path
from apps.login.views import login, logoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logoutView, name='logout'),
]
