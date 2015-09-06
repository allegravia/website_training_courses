from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_main_page, name='course_main_page'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
]

