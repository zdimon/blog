#coding: utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from blog.models import BlogCategory

class CategoryDetailView(DetailView):
    model = BlogCategory

def home(request):
    return render_to_response('home.html', {},context_instance=RequestContext(request))