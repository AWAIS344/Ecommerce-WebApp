from django import template

register = template.Library()

@register.filter
def to_int(value):
    """
    Safely convert value to int, or return 0 on error.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0
