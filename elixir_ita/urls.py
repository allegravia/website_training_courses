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
    url(r'^trainers/alberto_calderone$', views.trainer, {'trainer_name':'alberto_calderone', 'cn':'4'}, name='alberto_calderone'),
    url(r'^trainers/rita_casadio$', views.trainer, {'trainer_name':'rita_casadio', 'cn':'4'}, name='rita_casadio'),
    url(r'^trainers/gianni_cesareni$', views.trainer, {'trainer_name':'gianni_cesareni', 'cn':'4'}, name='gianni_cesareni'),
    url(r'^trainers/piero_fariselli$', views.trainer, {'trainer_name':'piero_fariselli', 'cn':'4'}, name='piero_fariselli'),
    url(r'^trainers/luana_licata$', views.trainer, {'trainer_name':'luana_licata', 'cn':'4'}, name='luana_licata'),
    url(r'^trainers/pierluigi_martelli$', views.trainer, {'trainer_name':'pierluigi_martelli', 'cn':'4'}, name='pierluigi_martelli'),
    url(r'^trainers/allegra_via$', views.trainer, {'trainer_name':'allegra_via', 'cn':'4'}, name='allegra_via'),
    url(r'^trainers/andreas_zanzoni$', views.trainer, {'trainer_name':'andreas_zanzoni', 'cn':'4'}, name='andreas_zanzoni'),
    #the two following urls do not work and I don't understand why
    #url(r'^trainers/(?P<trainer_name>allegra_via/)$', views.trainer, name="allegra_via"),
    #url(r'^trainers/(?P<trainer_name>\w+)/$', views.trainer),

]

