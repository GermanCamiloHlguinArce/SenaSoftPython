#Django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

#Views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
<<<<<<< HEAD
=======
    path('crear_citas/',CrearCitas.as_view(),name='crear_citas'),
>>>>>>> 351e6e4e696e8f398ad2d29a10f96da7c68baa8b
    path('eps/', include('appconsultaeps.urls')),
]
