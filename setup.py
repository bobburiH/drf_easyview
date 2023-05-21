from setuptools import setup

setup(
    name='django_easyview',
    version='1.0',
    description='Rapidly generate DRF API views for all models in your Django project. Simplifies development, but use with caution in production.',
    author='Haritha Bobburi',
    author_email='bobburih@gmail.com',
    url='https://github.com/bobburiH/django_easyview',
    packages=['django_easyview'],
    install_requires=[
        'Django',
        'djangorestframework',
        # Add any other dependencies required by your package
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
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
