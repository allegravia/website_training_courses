from django.conf.urls import url
from . import views

urlpatterns = [
#comment next line if you want elixir_ita_homepage to be the homepage
    url(r'^$', views.course_main_page, name='course_main_page'),
    url(r'^$', views.elixir_ita_homepage, name='elixir_ita_homepage'),
    url(r'^course$', views.course_main_page, name='course_main_page'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/(?P<pk>[0-9]+)/application$', views.application, name='application'),
    url(r'^course/(?P<pk>[0-9]+)/programme$', views.programme, name='programme'),
    url(r'^course/(?P<pk>[0-9]+)/material$', views.material, name='material'),
    url(r'^course$', views.unix, name='unix'),

]

