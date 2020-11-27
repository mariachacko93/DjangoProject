
from django.urls import path
from trainer.views import trainerRegistration,trainerlogin


urlpatterns = [
    path("trainerregistration",trainerRegistration),
    path("trainerlogin",trainerlogin),
]
