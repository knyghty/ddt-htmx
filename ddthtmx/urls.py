from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
]
