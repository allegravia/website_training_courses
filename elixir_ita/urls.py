from django.conf.urls import url
from . import views

urlpatterns = [
#comment next line if you want elixir_ita_homepage to be the homepage
#    url(r'^$', views.course_main_page, name='course_main_page'),
    url(r'^$', views.elixir_ita_homepage, name='elixir_ita_homepage'),
    url(r'^course$', views.course_main_page, name='course_main_page'),
    url(r'^events$', views.events, name='events'),
    url(r'^trainers$', views.trainers_main_page, name='trainers_main_page'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^excelerate_ttt$', views.excelerate_ttt, name='excelerate_ttt'),
    url(r'^TtT_at_BITS2016$', views.ttt_at_bits2016, name='ttt_at_bits2016'),
    url(r'^course_programme_2016$', views.course_programme_2016, name='course_programme_2016'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course_detail, name='course_detail'),
    url(r'^course/(?P<pk>[0-9]+)/application$', views.application, name='application'),
    url(r'^course/(?P<pk>[0-9]+)/programme$', views.programme, name='programme'),
    url(r'^course/(?P<pk>[0-9]+)/material$', views.material, name='material'),
    url(r'^course$', views.unix, name='unix'),
    url(r'^trainers/chiara_batini$', views.trainer, {'trainer_name':'chiara_batini', 'cn':'5'}, name='chiara_batini'),
    url(r'^trainers/alberto_calderone$', views.trainer, {'trainer_name':'alberto_calderone', 'cn':'4'}, name='alberto_calderone'),
    url(r'^trainers/vincenza_colonna$', views.trainer, {'trainer_name':'vincenza_colonna', 'cn':'5'}, name='vincenza_colonna'),
    url(r'^trainers/rita_casadio$', views.trainer, {'trainer_name':'rita_casadio', 'cn':'4'}, name='rita_casadio'),
    url(r'^trainers/gianni_cesareni$', views.trainer, {'trainer_name':'gianni_cesareni', 'cn':'4'}, name='gianni_cesareni'),
    url(r'^trainers/pietro_di_lena$', views.trainer, {'trainer_name':'pietro_di_lena', 'cn':'4'}, name='pietro_di_lena'),
    url(r'^trainers/piero_fariselli$', views.trainer, {'trainer_name':'piero_fariselli', 'cn':'4'}, name='piero_fariselli'),
    url(r'^trainers/luana_licata$', views.trainer, {'trainer_name':'luana_licata', 'cn':'4'}, name='luana_licata'),
    url(r'^trainers/pierluigi_martelli$', views.trainer, {'trainer_name':'pierluigi_martelli', 'cn':'4'}, name='pierluigi_martelli'),
    url(r'^trainers/allegra_via$', views.trainer, {'trainer_name':'allegra_via', 'cn':'5'}, name='allegra_via'),
    url(r'^trainers/andreas_zanzoni$', views.trainer, {'trainer_name':'andreas_zanzoni', 'cn':'4'}, name='andreas_zanzoni'),
    #the two following urls do not work and I don't understand why
    #url(r'^trainers/(?P<trainer_name>allegra_via/)$', views.trainer, name="allegra_via"),
    #url(r'^trainers/(?P<trainer_name>\w+)/$', views.trainer),

]

