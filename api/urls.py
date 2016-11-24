"""wishlist URL Configuration
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from viewsets import UserViewSet, BucketlistView, BucketlistDetail, BucketlisItemView, BucketlistItemUpdate, BucketlistItemDestroy


urlpatterns = [
    url(r'^bucketlists/$', BucketlistView.as_view(), name='create-bucketlists'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetail.as_view(), name='bucketlist-detail'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$', BucketlisItemView.as_view(), name='item-create'),
    url(r'^bucketlists/(?P<id>[0-9]+)/items/(?P<pk>[0-9]+)/$', BucketlistItemUpdate.as_view(), name='item-update'),
    url(r'^bucketlists/(?P<id>[0-9]+)/items/(?P<pk>[0-9]+)/$', BucketlistItemDestroy.as_view(), name='item-destroy'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
