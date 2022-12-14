from django.urls import re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/bathroom', views.BathroomViewSet)
router.register(r'api/review', views.ReviewViewSet)

urlpatterns = [
     re_path(r'^', include(router.urls)),
    # ex: /
    re_path(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    re_path(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /bathroom/
    re_path(r'^bathroom$', views.bathroom_list, name='bathroom_list'),
    # ex: /bathroom/5/
    re_path(r'^bathroom/(?P<bathroom_id>[0-9]+)/$', views.bathroom_detail, name='bathroom_detail'),
    re_path(r'^bathroom/(?P<bathroom_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),

]