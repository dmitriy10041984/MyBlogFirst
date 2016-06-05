from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.home', name='home'),
    #url(r'^about/$', 'blog.views.about', name='about'),
    #url(r'^contacts/$', 'blog.views.contacts', name='contacts'),
    #url(r'^article/(?P<article_id>[0-9]+)/$', 'blog.views.show_article', name='article'),
]