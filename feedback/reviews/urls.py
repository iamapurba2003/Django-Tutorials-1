from django.urls import path
from . import views

urlpatterns=[
    path("reviews/", views.reviews),
    path("thank-you/",views.thank_you)
]

