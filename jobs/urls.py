from django.urls import path
from .views import AddView

urlpatterns = [
    path('add/', AddView.as_view(), name='add-task'),
]
