=====================================
django_easyview Documentation
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   contributing
   license

=====================================
Installation
=====================================

To install the Django EasyView package, follow these steps:

1. Clone the package repository from `GitHub <https://github.com/bobburiH/django_easyview>`_.
2. Copy the contents of the ``django_easyview`` folder to your project directory.
3. Add ``'django_easyview'`` to the ``INSTALLED_APPS`` list in your project's settings file.
4. Include the package's URLs in your project's ``urls.py`` file:

   .. code-block:: python

      from django.urls import include, path

      urlpatterns = [
          # ... other URL patterns
          path('easyview/', include('django_easyview.urls')),
      ]

=====================================
Usage
=====================================

Once models are created, you can add the Django EasyView package to your Django project to automatically create an OpenAPI for all your models. With the reference provided by the package, you can start creating custom API views based on your business or personal requirements.

Here's how you can use the package to create your custom API views:

1. Ensure that the Django EasyView package is installed and added to your project as explained in the installation steps.

2. Start the development server by running the following command:

   .. code-block:: shell

      python manage.py runserver

3. Access the OpenAPI documentation for your models by appending ``/easyview/`` to the base URL of your Django project. For example, if your project is running at ``http://localhost:8000/``, the OpenAPI documentation will be available at ``http://localhost:8000/easyview/``.

4. Explore the available models and their corresponding endpoints in the OpenAPI documentation. This will provide you with the necessary information to create your custom API views.

5. Based on your requirements, you can create custom API views using Django Rest Framework's class-based views or function-based views. Refer to the Django Rest Framework documentation for detailed instructions on creating custom API views.

Database Migration
------------------

Before using the package, run the database migration command to create the necessary tables:

.. code-block:: shell

   python manage.py migrate

Starting the Server
-------------------

To start the development server and access the APIs provided by your models, use the following command:

.. code-block:: shell

   python manage.py runserver

Accessing the APIs
------------------

Once the server is running, you can access the APIs for your models by appending ``/easyview/`` to the base URL of your Django project.

For example, if your Django project is running at ``http://localhost:8000/``, you can access the APIs for your models at ``http://localhost:8000/easyview/``. The root of the API will provide a list of available models and their corresponding endpoints.

Please note that you should replace ``http://localhost:8000/`` with the actual base URL of your Django project.

=====================================
Contributing
=====================================

If you would like to contribute to the Django EasyView package, please refer to the `CONTRIBUTING.md <link-to-contributing-file>`_ file for guidelines.

=====================================
License
=====================================

The Django EasyView package is released under the `MIT License <./LICENSE>`_.

=====================================
Contact
=====================================

If you have any questions or feedback, please contact us at ``bobburih@gmail.com``.
