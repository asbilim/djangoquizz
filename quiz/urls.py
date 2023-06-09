from django.contrib import admin
from django.urls import path,include
from listings.views import home,login,register,signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="main-home-page"),
    path("auth/login",login,name="auth-login"),
    path("auth/register",register,name="auth-register"),
    path("logout",signout,name="logout"),
    path('quiz/',include('listings.urls'))
]
