from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    url(r'^$', 'website.views.home', name='home'),
    url(r'^amc/$', 'website.views.amc', name='amc'),
    url(r'^astro/$', 'website.views.astro', name='astro'),
    url(r'^cops/$', 'website.views.cops', name='cops'),
    url(r'^green/$', 'website.views.green', name='green'),
    url(r'^out/$', 'website.views.out', name='out'),
    url(r'^robo/$', 'website.views.robo', name='robo'),
    url(r'^sae/$', 'website.views.sae', name='sae'),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
