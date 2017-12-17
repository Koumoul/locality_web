from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.home, name='home'),

        url(r'^cultivateur/$', views.cultivateur_page, name='cultivateur_page'),
        url(r'^proprietaire/$', views.proprietaire_page, name='proprietaire_page'),

        url(r'^prop/$', views.signinProprietaireView, name='signinProprietaire'),
        url(r'^cult/$', views.signinCultivateurView, name='signinCultivateur'),

        url(r'^signin/$', views.signinView, name='signin'),
        url(r'^logout/$', views.logoutView, name='logout'),
        ]
