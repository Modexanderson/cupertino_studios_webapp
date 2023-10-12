from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apps/", views.app_list, name="app_list"),
    path('apps/<int:app_id>/select-os/', views.os_selection, name='os_selection'),
    path('apps/<int:app_id>/<str:os>/', views.app_detail, name='app_detail'),
]
