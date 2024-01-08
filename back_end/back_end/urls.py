from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("apps/", include("apps.urls")),
    path("admin/", admin.site.urls),
]