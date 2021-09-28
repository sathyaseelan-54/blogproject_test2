from django.urls import path
from .views import *


app_name = 'myapp'
urlpatterns = [

    path('',HomeView.as_view(),name = 'home'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('like/',Like_post,name = 'like-post'),

]