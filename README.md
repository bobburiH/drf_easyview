# django_easyview
Rapidly generate DRF API views for all models in your Django project. Simplifies development, but use with caution in production.
# Django EasyView

Django EasyView is a lightweight package that automates the creation of Django REST Framework (DRF) API views for all models in your Django project. With EasyView, you can effortlessly generate API endpoints and serializers, enabling seamless CRUD (Create, Retrieve, Update, Delete) operations for your models.

Simplify your development process and reduce boilerplate code by leveraging the power of Django EasyView. It provides an intuitive and efficient solution for quickly exposing your models as robust and customizable APIs, allowing you to focus on building your application's core functionalities.

**Key Features:**
- Automatic generation of API views and serializers for all models
- Support for standard CRUD operations (Create, Retrieve, Update, Delete)
- Seamless integration with Django and Django REST Framework
- Customizable options for fine-grained control over API behavior

Get started with Django EasyView today and streamline your API development workflow!

# Installation

# django_easyview

`django_easyview` is a package built on Django and Django REST Framework that provides easy-to-use views for your Django REST API.

## Installation

1. Clone the repository from GitHub:

    ```shell
    git clone https://github.com/bobburiH/django_easyview
    ```

2. copy folder inside cloned repository to root directory where project directory is located:

    ```shell
    dir django_easyview
    ```

3. Install the necessary prerequisites and dependencies, including Django and Django REST Framework:

    ```shell
    pip install django pip install djangorestframework
    ```

4. Add `'django_easyview'` to the `INSTALLED_APPS` list in your project's `settings.py` file:

    ```python
    INSTALLED_APPS = [
        # other apps
        'django_easyview',
    ]
    ```

5. Set up the URLs to include the `easyview` module in your project's `urls.py` file:

    ```python
    from django.urls import include, path
    from django_easyview import urls as easyview

    urlpatterns = [
        # other URL patterns
        path('', include(easyview)),
    ]
    ```

6. Run the migrations to create the necessary database tables for `django_easyview`:

    ```shell
    python manage.py migrate
    ```

Congratulations! You have successfully installed `django_easyview` and configured it for your Django project. By including `easyview` in your project's URLs, you will have the OpenAPI views ready to use.

Please make sure that Django and Django REST Framework are installed and properly set up in your project before proceeding with the installation of `django_easyview`.
7. Run server to create the necessary database tables for `django_easyview`:

   ```shell
    python manage.py runserver
   ```

open /easyapi endpoint on your local server and find all models api viewsets.
