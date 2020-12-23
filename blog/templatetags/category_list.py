from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('category_list.html')
def get_category_list():
    category_list = Category.objects.all()
    return {'category_list': category_list}


