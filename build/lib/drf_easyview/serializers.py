from rest_framework.serializers import ModelSerializer
from .utils import get_all_models


def generate_serializers():
    serializers = []
    for model in get_all_models():
        serializer_name = f"{model.__name__}Serializer"
        serializer_class = type(serializer_name, (ModelSerializer,), {
                                "Meta": type("Meta", (), {"model": model, "fields": "__all__"})})
        serializers.append(serializer_class)
    return serializers


# Generate serializers for all models
serializers = generate_serializers()
