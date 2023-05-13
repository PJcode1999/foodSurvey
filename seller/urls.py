from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'seller'

urlpatterns=[
    path("seller_form/", views.seller_form.as_view(), name="seller_form"),
]
 