#coding: utf-8
from django.conf.urls import patterns, include, url
from blog.views import CategoryDetailView
from blog.views import TopicDetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog-category/(?P<pk>\d+)/$', CategoryDetailView.as_view()),
    url(r'^blog-topic/(?P<pk>\d+)/$', TopicDetailView.as_view()),
    # url(r'^config/', include('config.foo.urls')),

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