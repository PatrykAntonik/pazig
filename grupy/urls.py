from django.urls import path
from .views import *

app_name = 'grupy'

urlpatterns = [
    path("", ListGroups.as_view(), name="all"),
    path("new", CreateGroup.as_view(), name="create"),
    path("new", CreateGroup.as_view(), name="create"),
    path("posts/in/<slug>", SingleGroup.as_view(), name="single"),
    path("posts/in/<slug>", JoinGroup.as_view(), name="join"),
    path("posts/in/<slug>", LeaveGroup.as_view(), name="leave"),
]
