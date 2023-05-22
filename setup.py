from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='drf_easyview',
    version='2.0.2',
    description='Rapidly generate DRF API views for all models in your Django project. Simplifies development, but use with caution in production.',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
