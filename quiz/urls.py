from django.contrib import admin
from django.urls import path
from listings.views import home,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="main-home-page"),
    path("auth/login",login,name="auth-login"),
]
