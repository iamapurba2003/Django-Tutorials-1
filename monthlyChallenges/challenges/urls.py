from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.challengeByNumber, name="intMonth"),
    path("<str:month>", views.monthlyChallenge, name="strMonth"),
]
