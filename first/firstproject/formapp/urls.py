from django.urls import path
from formapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form/', views.form_name_view, name="form"),
]
