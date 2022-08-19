from django.urls import re_path
from . import views

urlpatterns = [
    # ex: /
    re_path(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    re_path(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    re_path(r'^bathroom$', views.bathroom_list, name='bathroom_list'),
    # ex: /wine/5/
    re_path(r'^bathroom/(?P<bathroom_id>[0-9]+)/$', views.bathroom_detail, name='bathroom_detail'),
]