from django import template

register = template.Library()

def simplepaginator(context, adjacent_pages=2):

    page_numbers = [n for n in \
                    range(context["page_obj"].number - adjacent_pages, context["page_obj"].number + adjacent_pages + 1) \
                    if n > 0 and n <= context["paginator"].num_pages]

    return {
        "page_obj": context["page_obj"],
        "paginator" : context["paginator"],
        "page_numbers" : page_numbers
    }

register.inclusion_tag("simplepaginator.html", takes_context=True)(simplepaginator)
