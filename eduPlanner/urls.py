from django.contrib import admin
from django.urls import path, include
from eventos import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventos.urls')),  
    path('programaApi/', include('programaApi.urls')),
    path('calendario_admin.html', views.calendario_admin, name='administracion'),
    
]
