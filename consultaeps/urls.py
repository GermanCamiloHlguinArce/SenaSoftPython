#Django
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView

#Views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('app/',include('appconsultaeps.urls'))
]
