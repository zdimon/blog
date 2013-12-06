#coding: utf-8
import os
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
from django.conf.urls import patterns, include, url
from blog.views import CategoryDetailView
from blog.views import TopicDetailView, TopicListView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog-category/(?P<pk>\d+)/$', CategoryDetailView.as_view()),
    url(r'^blog-topic/(?P<pk>\d+)/$', TopicDetailView.as_view()),

    url(r'^blog-topic-list/(?P<pk>\d+)/$', TopicListView.as_view(template_name = 'blogtopic_list.html'), name='blog-topic-list'),

    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^elfinder/', include('elfinder.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from config.settings import DEBUG, MEDIA_ROOT
if DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
        }),
   )

