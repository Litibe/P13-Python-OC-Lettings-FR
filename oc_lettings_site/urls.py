from django.contrib import admin
from django.urls import path, include

from . import views

admin.site.site_header = "Orange Country Lettings"
admin.site.site_title = "Orange Country Lettings Admin"
admin.site.index_title = "Welcome to Orange Country Lettings"


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.handler500"

urlpatterns = [
    path('', views.index, name='oc_lettings_site_index'),
    path('admin/', admin.site.urls),
    path('lettings/', include("lettings.urls", namespace='lettings')),
    path('profiles/', include("profiles.urls", namespace='profiles')),
    path('sentry-debug/', trigger_error),
]
