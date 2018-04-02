from django.conf.urls import url
from website import views
from django.views.generic import RedirectView

urlpatterns = [

    # Home
    url(r'^home$', views.home, name='home'),
    url(r'^home/([0-9]+)$', views.home, name='home'),

    # Service
    url(r'^service$', views.service, name='service'),
    url(r'^service/to_airklass$', views.to_airklass, name='to_airklass'),
    url(r'^service/to_login$', views.to_login, name='to_login'),

    # Recruit
    url(r'^recruit$', views.recruit, name='recruit'),
    url(r'^recruit/apply$', views.apply_recruit, name='apply_recruit'),


    # Contact
    url(r'^contact$', views.contact, name='contact'),
]
