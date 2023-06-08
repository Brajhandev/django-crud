from django.urls import include, path
from rest_framework import routers
from clients import views

router = routers.DefaultRouter()
router.register(r"clients", views.ClientView, "clients")

urlpatterns = [
    path("api/v1/", include(router.urls)),    
]