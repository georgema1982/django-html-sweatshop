=====================
django-html-sweatshop
=====================

Some common html renderings are tedious. Let django-html-sweatshop do the hard work.

Features
========

- Digg style pagination with optional integration with django-tables2

- Display messages

- Pop up confirmation dialog before deleting

Installation
============

To get started using ``django-html-sweatshop``:

- install it with ``pip``::

    $ pip install django-html-sweatshop

- add the app to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'html_sweatshop',
    	'django_tables2', #Required if you need digg style pagination
        ...
    )

Digg Style Pagination
=====================

A set of tags are provided to render digg style pagination. To use these tags, load them in the template

	{% load digg_pagination_tags %}

Raw Pagination
--------------

Usage::

	{% digg_paginator page_obj page_field theme %}

This is the raw way to render pagination. You have to take care of actual work of pagination (some generic view can do that part of work for you) as outlined in https://docs.djangoproject.com/en/1.9/topics/pagination/. This tag will take care of the rendering of pagination. It provides greater flexibility than the other two.

``page_obj``

	Optional. A page object as outlined in https://docs.djangoproject.com/en/1.9/topics/pagination/#page-objects. By default, a variable named "page_obj" in the context will be used if it's not provided.

``page_field``

	Optional. The name of the page parameter in the url. For example, if "page_field" is set to "page", when the link of the second page is clicked, "page=2" will be appended to the url. The default value is "page".

``theme``

	Optional. The theme pack to use. Right now Bootstrap 3 is the only valid theme available. So there's no need to set this parameter.

Django-table2 Integration
------------------------------

Usage::

	{% digg_paginator_tables2 table theme %}

This tag provides integration with django-tables2. It's usually used along side with the SingleTableView generic view shipped with django-tables2. But the tables rendered by django-tables2 tag might look alien with the pagination without overriding the default table template.

``table``

	Optional. A table instance of django-tables2. Please refer to django-tables2 document regarding table class. By default, a variable named "table" in the context will be used if it's not provided.

``theme``

	Optional. The theme pack to use. Right now Bootstrap 3 is the only valid theme available. So there's no need to set this parameter.

Django-table2 Seamless Integration
----------------------------------

Usage::

	{% render_paginated_table table theme %}

This tag provides seamless integration with django-tables2. Unlike the other two tags which only render pagination, this tag render table and pagination altogether.

``table``

	Optional. A table instance of django-tables2. Please refer to django-tables2 document regarding table class. By default, a variable named "table" in the context will be used if it's not provided.

``theme``

	Optional. The theme pack to use. Right now Bootstrap 3 is the only valid theme available. So there's no need to set this parameter.
