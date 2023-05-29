from django.urls import path
from .views import *

app_name = 'grupy'

urlpatterns = [
    path("", ListGroups.as_view(), name="all"),
    path("new", CreateGroup.as_view(), name="create"),
    path("posts/in/<slug>", SingleGroup.as_view(), name="single"),
    path("join/in/<slug>/", JoinGroup.as_view(), name="join"),
    path("leave/in/<slug>/", LeaveGroup.as_view(), name="leave"),
]
