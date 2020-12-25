from django.urls import path

from .views import OwnerCreateView, OwnerDetailView, OwnerListView

urlpatterns = [
    path('owners/', OwnerListView.as_view()),
    path('owners/<int:pk>/', OwnerDetailView.as_view()),
    path('owners/new/', OwnerCreateView.as_view()),
]