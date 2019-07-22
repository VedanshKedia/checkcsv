from django.urls import path
from . import views


urlpatterns = [
    path('', views.form_upload, name='document_form'),
    path('home/', views.home, name='home'),
]
