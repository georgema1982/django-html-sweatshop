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

Message Centre
==============

A tag to display all the messages with meaningful background color and icons. To use this tag, load it in the template

	{% load message_centre_tags %}

Then at where you want to display the messages

	{% message_centre dismissible theme %}

``dismissible``

	Optional. A boolean value to indicate if the messages are dissmissible (depending on the theme pack). By default, its value is HTML_SWEATSHOP_MESSAGE_CENTRE_MESSAGE_DISMISSIBLE which defaults to True.

``theme``

	Optional. The theme pack to use. Right now Bootstrap 3 is the only valid theme available. So there's no need to set this parameter.

One Step Delete
===============

DeleteView generic view makes deletion a two step process. First step, a confirmation page is rendered. Second step, the deletion is submitted. But in most systems, it's more desirable to simply pop up a confirmation modal before submitting the deletion, all happening on the same page.

A tag and a Jquery plugin are provided to make it simpler.

Load the tag definition
-----------------------

	{% load one_step_delete_tags static %}

Load the JQuery plugin
----------------------

Load the JQuery plugin at where js should be included. It's your own responsibility to include JQuery itself.

	{% include_one_step_delete_js %}
	
	<script type="text/javascript" src="{% static 'one_step_delete/js/init_one_step_delete.js' %}"></script>

Render delete buttons
---------------------

Render delete buttons depending on the theme pack. Take Bootstrap 3 theme as an example, a delete button can be

	<button class="btn btn-danger" data-toggle="modal" data-target="..." data-modal-title="..." data-modal-action="..." data-obj-description="...">...</button>

A few JQuery plugin specific data properties can be defined to allow multiple delete buttons to share the same confirmation modal.

``data-modal-title``

	Replace the modal title with this value when the button is clicked.

``data-modal-action``

	Replace the action url of deletion submission with this value when the button is clicked.

``data-obj-description``

	If you are satisfied with the overall message in the modal body, you can replace the description of the object to delete with this value to fine tune the message when the button is clicked. 

``data-body``

	Replace the message of the modal body with this value totally when the button is clicked.

Render confirmation modals
--------------------------

Use the following tag to render the confirmation modal. You can render each confirmation modal for each delete button or you can render one to be shared among delete buttons.

	{% render_confirm_modal dialog_id obj obj_description url title body theme %}

``dialog_id``

	Optional. The HTML id of the confirmation modal. Defaults to "confirmation-modal".

``obj``

	Optional. A model object to be deleted. Once provided, a default confirmation message can be inferred by the tag.

``obj_description``

	Optional. The default confirmation message use the verbose name of "obj" as the description. It can be overridden by this parameter.

``url``

	Optional. The action url delete is submitted to. By default it's empty.

``title``

	Optional. The title of the confirmation modal. By default, it's "Are you sure?"

``body``

	Optional. Used to override the whole default confirmation message.

``theme``

	Optional. The theme pack to use. Right now Bootstrap 3 is the only valid theme available. So there's no need to set this parameter.

Settings
========

``HTML_SWEATSHOP_DIGG_PAGINATION_LEADING_PAGE_RANGE_DISPLAYED``

	Defaults to 10

``HTML_SWEATSHOP_DIGG_PAGINATION_TRAILING_PAGE_RANGE_DISPLAYED``

	Defaults to 10

``HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE``

	Defaults to 2

``HTML_SWEATSHOP_DIGG_PAGINATION_LEADING_PAGE_RANGE``

	Defaults to 8

``HTML_SWEATSHOP_DIGG_PAGINATION_TRAILING_PAGE_RANGE``

	Defaults to 8

``HTML_SWEATSHOP_DIGG_PAGINATION_ADJACENT_PAGES``

	Defaults to 4

``HTML_SWEATSHOP_THEME``

	The theme pack to use. Defauls to 'bootstrap3'

``HTML_SWEATSHOP_MESSAGE_CENTRE_MESSAGE_DISMISSIBLE``

	If the messages are dimissible. Defaults to True

Demo
====

Checkout the source codes. Inside the source codes folder, run the following commands:

	mkvirtualenv demo
	
	pip install -r requirements.txt
	
	python manage.py runserver

How to contribute
=================

Fork the project and submit pull requests. Need more theme packs.