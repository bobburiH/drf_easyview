from rest_framework.viewsets import ModelViewSet
from .utils import get_all_models
from .serializers import *


def generate_viewsets():
    viewsets = []
    for model in get_all_models():
        serializer_name = f"{model.__name__}Serializer"
        serializer_class = type(
            serializer_name, (ModelSerializer,), {"Meta": type(
                "Meta", (), {"model": model, "fields": "__all__"})}
        )
        viewset_name = f"{model.__name__}ViewSet"
        viewset_class = type(viewset_name, (ModelViewSet,), {
                             "queryset": model.objects.all(), "serializer_class": serializer_class})
        viewsets.append(viewset_class)
    return viewsets


# Generate viewsets for all models
viewsets = generate_viewsets()
