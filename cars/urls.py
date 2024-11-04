from django.urls import path
from .views import HomeView, CustomLoginView, CustomLogoutView, DetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home_page'),  # Added missing comma here
     path('car-detail/<int:pk>/', DetailView.as_view(), name='detail_page'),
]
