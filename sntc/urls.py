from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website import views as web_views

urlpatterns = [
    url(r'^$', web_views.home, name='home'),
    url(r'^amc/$', web_views.amc, name='amc'),
    url(r'^astro/$', web_views.astro, name='astro'),
    url(r'^cops/$', web_views.cops, name='cops'),
    url(r'^green/$', web_views.green, name='green'),
    url(r'^out/$', web_views.out, name='out'),
    url(r'^robo/$', web_views.robo, name='robo'),
    url(r'^sae/$', web_views.sae, name='sae'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
