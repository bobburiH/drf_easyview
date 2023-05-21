from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import viewsets

router = DefaultRouter()
for viewset in viewsets:
    model_name = viewset.serializer_class.Meta.model.__name__.lower()
    router.register(model_name, viewset)

urlpatterns = [
    path('easyapi/', include(router.urls)),
]
