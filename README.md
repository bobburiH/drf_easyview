# django_easyview
Rapidly generate DRF API views for all models in your Django project. Simplifies development, but use with caution in production.

[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://django-easyview.readthedocs.io)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/bobburiH/django_easyview/blob/master/LICENSE)

# Django EasyView
The Django DRF Package is a convenient package designed to simplify the integration of Django and Django Rest Framework (DRF). It provides tools and utilities that automate common tasks, such as model registration with the admin site, generation of serializers and viewsets, and setup of URL patterns for API endpoints.


Django EasyView is a lightweight package that automates the creation of Django REST Framework (DRF) API views for all models in your Django project. With EasyView, you can effortlessly generate API endpoints and serializers, enabling seamless CRUD (Create, Retrieve, Update, Delete) operations for your models.

Simplify your development process and reduce boilerplate code by leveraging the power of Django EasyView. It provides an intuitive and efficient solution for quickly exposing your models as robust and customizable APIs, allowing you to focus on building your application's core functionalities.

**Key Features:**
- Automatic generation of API views and serializers for all models
- Support for standard CRUD operations (Create, Retrieve, Update, Delete)
- Seamless integration with Django and Django REST Framework
- Customizable options for fine-grained control over API behavior

Get started with Django EasyView today and streamline your API development workflow!

# Django DRF Package

## Overview
The Django DRF Package is a convenient package designed to simplify the integration of Django and Django Rest Framework (DRF). It provides tools and utilities that automate common tasks, such as model registration with the admin site, generation of serializers and viewsets, and setup of URL patterns for API endpoints.

## Installation
To install the Django DRF Package, follow these steps:

1. Clone the package repository from [GitHub](https://github.com/bobburiH/django_easyview).
2. Copy the contents of the `django_easyview` folder to your project directory.
3. Add `'django_easyview'` to the `INSTALLED_APPS` list in your project's settings file.
4. Include the package's URLs in your project's `urls.py` file:

        from django.urls import include, path
   
        urlpatterns = [
            # ... other URL patterns
            path('easyview/', include('django_easyview.urls')),
        ]

## Usage
Once models are created, you can add this package to your Django project to automatically create an OpenAPI for all your models. With the reference provided by the package, you can start creating custom API views based on your business or personal requirements.

Here's how you can use the package to create your custom API views:

1. Ensure that the Django DRF Package is installed and added to your project as explained in the installation steps.

2. Start the development server by running the following command:

        python manage.py runserver

3. Access the OpenAPI documentation for your models by appending `/easyview/` to the base URL of your Django project. For example, if your project is running at `http://localhost:8000/`, the OpenAPI documentation will be available at `http://localhost:8000/easyview/`.

4. Explore the available models and their corresponding endpoints in the OpenAPI documentation. This will provide you with the necessary information to create your custom API views.

5. Based on your requirements, you can create custom API views using Django Rest Framework's class-based views or function-based views. Refer to the Django Rest Framework documentation for detailed instructions on creating custom API views.


### Database Migration
Before using the package, run the database migration command to create the necessary tables:

    ```shell
    python manage.py migrate
    ```

### Starting the Server
To start the development server and access the APIs provided by your models, use the following command:

    ```shell
    python manage.py runserver
    ```

### Accessing the APIs
Once the server is running, you can access the APIs for your models by appending `/easyview/` to the base URL of your Django project.

For example, if your Django project is running at `http://localhost:8000/`, you can access the APIs for your models at `http://localhost:8000/easyview/`. The root of the API will provide a list of available models and their corresponding endpoints.

Please note that you should replace `http://localhost:8000/` with the actual base URL of your Django project.

## Contributing
If you would like to contribute to the Django DRF Package, please refer to the [CONTRIBUTING.md](link-to-contributing-file) file for guidelines.

## License
The Django DRF Package is released under the [MIT License](./LICENSE).

## Contact
If you have any questions or feedback, please contact us at [bobburih@gmail.com].

## Documentation

The latest documentation for this project can be found at [django-easyview.readthedocs.io](https://django-easyview.readthedocs.io).