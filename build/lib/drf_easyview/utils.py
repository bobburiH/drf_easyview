from django.apps import apps


def get_all_models():
    models = []
    for app_config in apps.get_app_configs():
        models.extend(app_config.get_models())
        print(models)
    return models
