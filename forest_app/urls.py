from django.urls import path
from .views import StartScreenView

urlpatterns = [
    path('', StartScreenView.as_view(), name='start_screen'),
]
