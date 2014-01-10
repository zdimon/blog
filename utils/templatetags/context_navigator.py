from django import template
from blog.models import BlogCategory, BlogTopic
register = template.Library()

@register.inclusion_tag("context_navigator.html", takes_context = True)
def context_navigator(context):
    request = context['request']
    par = {}
    c = BlogCategory.objects.all()
    par['cats'] = c
    if 'cur_cat' in request.session:
        par['category'] = request.session['cur_cat']
    return par


