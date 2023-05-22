from setuptools import setup

setup(
    name='drf_easyview',
    version='2.0.1',
    description='Rapidly generate DRF API views for all models in your Django project. Simplifies development, but use with caution in production.',
    long_description='Once models are created, you can add the Django EasyView package to your Django project to automatically create an OpenAPI for all your models. With the reference provided by the package, you can start creating custom API views based on your business or personal requirements.',
    author='Haritha Bobburi',
    author_email='bobburih@gmail.com',
    url='https://github.com/bobburiH/drf_easyview',
    packages=['drf_easyview'],
    install_requires=[
        'django',
        'djangorestframework',
        # Add any other dependencies required by your package
    ],
    keywords='django drf package django-rest-framework authentication permissions REST API web development',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
