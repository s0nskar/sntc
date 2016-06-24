from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from website import views as web_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', web_views.home, name='home'),
    url(r'^subscribe/$', web_views.subscribe, name='subscribe'),
    url(r'^(?P<slug>[\w\-]+)/$', web_views.club, name='club'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
