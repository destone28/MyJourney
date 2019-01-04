from django import template

register = template.Library()

@register.filter
def get_index(ls, value):
  return list(ls).index(value)
