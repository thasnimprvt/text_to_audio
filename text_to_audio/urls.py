from django.urls import path
from .views import ReadTextView

urlpatterns = [
    path('text/', ReadTextView.as_view()),
]