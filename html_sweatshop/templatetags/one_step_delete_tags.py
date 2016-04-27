from django import template
from html_sweatshop.conf import settings
from django.db import models

register = template.Library()

@register.inclusion_tag('one_step_delete/delete_confirm_dialog.html', takes_context = True)
def render_confirm_modal(context, dialog_id = 'confirmation-modal', obj = '', obj_description = '', url = '', title = '', body = '', theme = settings.HTML_SWEATSHOP_THEME):
    if not obj and not obj_description and not body: raise Exception('Default message cannot be inferred as obj, obj_description and body are all empty.')
    if not obj_description and not body and obj and isinstance(obj, models.Model): obj_description = obj._meta.verbose_name
    variables = locals()
    variables.pop('context')
    variables.update(dialog_template = 'one_step_delete/themes/%s.html' % theme, csrf_token = context['csrf_token'])
    return variables

@register.inclusion_tag('one_step_delete/include_js.html')
def include_one_step_delete_js(theme = settings.HTML_SWEATSHOP_THEME):
    return {'js_name': 'one_step_delete/js/themes/%s/jquery.one-step-delete.js' % theme}
