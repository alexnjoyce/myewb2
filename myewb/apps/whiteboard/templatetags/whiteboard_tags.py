from django.template import Library
from django.conf import settings

register = Library()

@register.inclusion_tag("whiteboard/whiteboard.html", takes_context=True)
def show_whiteboard(context, whiteboard, group, member):
    """
    Show a whiteboard.  If the whiteboard is empty, show a link to create one.
    """
    return {
        "wb": whiteboard,
        "group": group,
        "member": member,
        "force": False,
        "STATIC_URL": settings.STATIC_URL,
        "request": context['request']
    }

@register.inclusion_tag("whiteboard/whiteboard.html", takes_context=True)
def show_whiteboard_force(context, whiteboard, group, member):
    """
    Show a whiteboard, even if it's empty.
    """
    return {
        "wb": whiteboard,
        "group": group,
        "member": member,
        "force": True,
        "STATIC_URL": settings.STATIC_URL,
        "request": context['request']
    }

