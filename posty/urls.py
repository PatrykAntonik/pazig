from django.urls import path
from .views import *

app_name = 'posty'

urlpatterns = [
    path('',PostList.as_view(),name='all'),
    path('new/',CreatePost.as_view(),name='create'),
    path('by/<username>/',UserPost.as_view(),name='for_user'),
    path('by/<username>/<int:pk>/',PostDetail.as_view(),name='single'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete'),
]
