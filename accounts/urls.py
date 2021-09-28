from django.urls import path

from .views import *

urlpatterns = [

    path('sign/', SignUpView.as_view(), name='signup'),

]