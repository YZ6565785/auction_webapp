from django.conf import settings
from django.conf.urls import include, url
#newer version of django url dispather
from django.urls import path
from django.contrib import admin






urlpatterns = [
    path(r'', include('welcome.urls')),
    path(r'^health$', lambda request: HttpResponse('okay')),
    path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
