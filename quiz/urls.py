from django.contrib import admin
from django.urls import path,include
from listings.views import home,login,register,signout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="main-home-page"),
    path("auth/login",login,name="auth-login"),
    path("auth/register",register,name="auth-register"),
    path("logout",signout,name="logout"),
    path('quiz/',include('listings.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)