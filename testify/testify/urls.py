from django.contrib import admin
from django.urls import include, path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('form-view/', views.form_view, name='form_view'),
]
