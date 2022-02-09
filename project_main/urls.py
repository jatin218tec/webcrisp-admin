from django.contrib import admin
from django.urls import path, include
from . import views as webcrisp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', webcrisp_views.index, name='index'),
    path('project', webcrisp_views.project, name='project')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
