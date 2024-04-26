from django.contrib import admin
from django.urls import include, path
from app import views
from app.views.create_test import create_test_view
from app.views.enter_test import enter_code_view, submit_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('form-view/', views.form_view, name='form_view'),
    path('create-test/', create_test_view, name='create-test'),
    path('enter-code/<str:code>/', enter_code_view, name='enter_code_view'),
    path('submit-test/', submit_test_view, name='submit-test'),
]
