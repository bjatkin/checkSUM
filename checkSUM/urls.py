from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('bundle.css', views.bundle_css, name='bundle_css'),
    path('bundle.js', views.bundle_js, name='bundle_js'),
    path('database/', views.dataBase)
]