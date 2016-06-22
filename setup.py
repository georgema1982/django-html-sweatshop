from setuptools import setup, find_packages


setup(
    name="django-html-sweatshop",
    version="0.1.0",
    url='https://github.com/georgema1982/django-html-sweatshop',
    license='MIT',
    description="A Django app that simplifies some common HTML rendering",
    long_description=open('README.rst').read(),
    author='George Ma',
    author_email='george.ma1982@gmail.com',
    packages=find_packages(exclude = ['example']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django-tables2==1.0.4',
        'django-appconf',
    ],
    include_package_data=True,
    zip_safe=False,
)
