from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tourist_attractions/', include('tourist_attractions.urls')),
    path('admin/', admin.site.urls),
]