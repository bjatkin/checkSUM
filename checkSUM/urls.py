from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('bundle.css', views.bundle_css, name='bundle_css'),
    path('bundle.js', views.bundle_js, name='bundle_js'),
    path('request_login', views.request_login, name="request_login"),
    path('create_account', views.create_account, name="create_account"),
    path('get_account_info', views.get_account_info, name="get_account_info"),
    path('is_email_available', views.is_email_available, name="is_email_aailable"),
    path('store_secret', views.store_secret, name="store_secret"),
    path('verify_age', views.verify_age, name="verify_age"),
    path('request_fname', views.request_fname, name="request_fname"),
]