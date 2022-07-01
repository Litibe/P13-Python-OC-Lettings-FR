from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "Orange Country Lettings"
admin.site.site_title = "Orange Country Lettings Admin"
admin.site.index_title = "Welcome to Orange Country Lettings"

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('profiles/', views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
