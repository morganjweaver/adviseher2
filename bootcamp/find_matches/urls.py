from django.conf.urls import url
from . import views

appname = 'find_matches'
urlpatterns = [
    url(r'^$', views.index, name='mentor_find_index'),
    url(r'^(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
]