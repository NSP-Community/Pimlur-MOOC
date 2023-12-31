"""PimlurMOOC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import django_comments_xtd_views
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("dashboard/", include("dashboard.urls")),
    path("project/", include("project.urls")),
    path('comments', views.comments, name="comments"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('messages/', include('django_messages.urls')),
    path('comments/', include("django_comments_xtd.urls")),
    # API handlers.
    path('api/', include("django_comments_xtd.api.urls"),
         {'override_drf_defaults': True}),
    path('', include("django_comments.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)