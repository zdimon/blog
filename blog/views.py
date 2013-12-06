#coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from blog.models import BlogCategory
from blog.models import BlogTopic
from utils import filterMixin

class CategoryDetailView(DetailView):
    model = BlogCategory
    template_name = 'blogcategory_detail.html'


class TopicDetailView(DetailView):
    model = BlogTopic
    template_name = 'blogtopic_detail.html'

class TopicListView(ListView):
    model = BlogTopic
    paginate_by = 6
    def get_queryset(self):
        qs = self.model.objects.all()
        #search = self.request.GET.get('pk')
        search = self.kwargs

        if search['pk']:
            qs = qs.filter(category=int(search['pk']))
            self.request.session['cur_cat'] = int(search['pk'])
        qs.order_by("-id")
        return qs

def home(request):
    return render_to_response('home.html', {},context_instance=RequestContext(request))
