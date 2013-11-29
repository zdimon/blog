#-*- coding: utf-8 -*-
from django import template
from blog.models import BlogCategory
# экземпляр класса, в котором все наши теги будут зарегистрированы
register = template.Library()
# регистрируем наш тег, который будет выводить шаблон sidebar.html
@register.inclusion_tag("sidebar.html", takes_context = True)
def show_sidebar(context):
    cats = BlogCategory.objects.all()
    request = context['request']
    return {'cats': cats, 'request': request}
