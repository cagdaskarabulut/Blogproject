from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'^$', posts_list,name='post-list'),
    url(r'^testBos/$', testBos),
    url(r'^test/$', test),
    url(r'^post_detail/(?P<slug>[-\w]+)/$', post_detail,name='post-detail'),
    url(r'^post_create/$', post_create,name='post-create'),
    url(r'^post_update/(?P<slug>[-\w]+)/$', post_update,name='post-update'),
    url(r'^post_delete/(?P<slug>[-\w]+)/$', post_delete,name='post-delete'),
    url(r'^sanatcilar/(?P<sayi>[0-9a-z]+)/',sanatcilar),
]