from django.urls import path

from . import views, views_property, views_tenant, views_units


urlpatterns = [
    path("", views.index, name="index"),
    path("property", views_property.property, name="property"),
    path("tenant", views_tenant.tenant, name="tenant"),
    path("tenant", views_tenant.tenant, name="tenant"),
    path("units", views_units.units, name="units")
]