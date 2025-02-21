from django import template


register = template.Library()


@register.filter
def get_filename(filename: str):
    name = filename.split('/')[-1]
    return name
