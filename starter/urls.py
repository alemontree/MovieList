from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()


from .views import (
    landing_page,
    movie_detail,
    )


urlpatterns = [
    url(r'^$', landing_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<id>\d+)/$', movie_detail)
]

urlpatterns += staticfiles_urlpatterns()

