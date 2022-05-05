from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from suriatech import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route = '',
        view = views.index,
        name = 'inicio'
    )
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
