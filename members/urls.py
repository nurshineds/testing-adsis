from django.urls import path
from . import views

urlpatterns = [
    path("our-teams/", views.members, name="members")
]
