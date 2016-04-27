from django import template
from html_sweatshop.conf import settings

register = template.Library()

@register.inclusion_tag('message_centre/messages.html', takes_context = True)
def message_centre(context, dismissible = settings.HTML_SWEATSHOP_MESSAGE_CENTRE_MESSAGE_DISMISSIBLE, theme = settings.HTML_SWEATSHOP_THEME):
    return {
        'messages': context['messages'],
        'dismissible': dismissible,
        'template': 'message_centre/themes/%s.html' % theme
    }