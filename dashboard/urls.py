from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("<category>", views.dashboard_category, name="dashboard_category"),
    path('/join_pimlur', views.join_pimlur, name="join_pimlur"),
]
