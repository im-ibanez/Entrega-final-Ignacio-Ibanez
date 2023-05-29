from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("index", views.index, name="index"),
    path('register', views.register, name='Register'), # type: ignore
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
