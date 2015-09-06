from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_main_page, name='course_main_page'),
]
