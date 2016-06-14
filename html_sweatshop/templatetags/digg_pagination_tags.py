from html_sweatshop.conf import settings
from django import template

register = template.Library()

def paginator(context, page_obj, page_field, theme):
    paginator = page_obj.paginator
    pages = paginator.num_pages
    page = page_obj.number
    in_leading_range = in_trailing_range = False
    pages_outside_leading_range = pages_outside_trailing_range = range(0)
    if pages <= settings.HTML_SWEATSHOP_DIGG_PAGINATION_LEADING_PAGE_RANGE_DISPLAYED + settings.HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE + 1:
        in_leading_range = in_trailing_range = True
        page_range = [n for n in range(1, pages + 1)]
    elif page <= settings.HTML_SWEATSHOP_DIGG_PAGINATION_LEADING_PAGE_RANGE:
        in_leading_range = True
        page_range = [n for n in range(1, settings.HTML_SWEATSHOP_DIGG_PAGINATION_LEADING_PAGE_RANGE_DISPLAYED + 1)]
        pages_outside_leading_range = [n + pages for n in range(0, -settings.HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE, -1)]
    elif page > pages - settings.HTML_SWEATSHOP_DIGG_PAGINATION_TRAILING_PAGE_RANGE:
        in_trailing_range = True
        page_range = [n for n in range(pages - settings.HTML_SWEATSHOP_DIGG_PAGINATION_TRAILING_PAGE_RANGE_DISPLAYED + 1, pages + 1) if n > 0 and n <= pages]
        pages_outside_trailing_range = [n + 1 for n in range(0, settings.HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE)]
    else: 
        page_range = [n for n in range(page - settings.HTML_SWEATSHOP_DIGG_PAGINATION_ADJACENT_PAGES, page + settings.HTML_SWEATSHOP_DIGG_PAGINATION_ADJACENT_PAGES + 1) if n > 0 and n <= pages]
        pages_outside_leading_range = [n + pages for n in range(0, -settings.HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE, -1)]
        pages_outside_trailing_range = [n + 1 for n in range(0, settings.HTML_SWEATSHOP_DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE)]
    return {
        'request': context['request'],
        'pages': pages,
        'page': page,
        'previous': page_obj.has_previous() and page_obj.previous_page_number() or 1,
        'next': page_obj.has_next() and page_obj.next_page_number() or page_obj.end_index(),
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'page_range': page_range,
        'in_leading_range': in_leading_range,
        'in_trailing_range': in_trailing_range,
        'pages_outside_leading_range': pages_outside_leading_range,
        'pages_outside_trailing_range': pages_outside_trailing_range,
        'page_field': page_field,
        'pagination_template': 'digg_pagination/themes/%s.html' % theme,
    }

@register.inclusion_tag('digg_pagination/digg_paginator.html', takes_context=True)
def digg_paginator(context, page_obj = None, page_field = 'page', theme = settings.HTML_SWEATSHOP_THEME):
    return paginator(context, page_obj or template.Variable('page_obj').resolve(context), page_field, theme)

@register.inclusion_tag('digg_pagination/digg_paginator.html', takes_context=True)
def digg_paginator_tables2(context, table = None, theme = settings.HTML_SWEATSHOP_THEME):
    return paginator(context, table and table.page or template.Variable('table.page').resolve(context), table and table.prefixed_page_field or template.Variable('table.prefixed_page_field').resolve(context), theme)

@register.inclusion_tag('django_tables2/paginated_table.html', takes_context=True)
def render_paginated_table(context, table = None, theme = settings.HTML_SWEATSHOP_THEME):
    return {
        'request': context['request'],
        'table': table or template.Variable('table').resolve(context),
        'template': 'django_tables2/themes/%s.html' % theme
    }