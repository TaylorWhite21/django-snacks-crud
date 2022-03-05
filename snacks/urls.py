from django.urls import path
from django.shortcuts import render
from .views import *

urlpatterns = [
  path('', SnackListView.as_view(), name='snack-list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack-detail'),
  path('new/',SnackCreateView.as_view(), name='snack-create'),
	path('<int:pk>/delete',SnackDeleteView.as_view(), name='snack-delete'),
	path('<int:pk>/edit',SnackUpdateView.as_view(), name='snack-update')
]
