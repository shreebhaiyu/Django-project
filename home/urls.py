from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('^amazon/$', views.amazon, name='amazon'),
    url('^hulu/$', views.hulu, name='hulu'),
    url('^netflixusa/$', views.netflix, name='index'),
    url('^netflixusa/stephen/$', views.netflix_stephen, name='index'),
    url('^netflixusa/mom/$', views.netflix_mom, name='index'),
    url('^netflixusa/dad/$', views.netflix_dad, name='index'),
]






