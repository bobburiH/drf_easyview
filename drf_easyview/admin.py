from django.contrib import admin
from django.apps import apps

# Get all models from installed apps
models = apps.get_models()

# Register all models with the admin site
for model in models:
    admin.site.register(model)
