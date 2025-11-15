from django.urls import path
from profile_app import views

app_name = 'profile_app'
urlpatterns = [
    
    # Home.
    path('', views.home_view, name="home"),
    # Dashboard.
    path('dashboard/', views.dashboard_view, name="dashboard"),
    # Detail Profile.
    path('profile/<int:pk>', views.profile_view, name="profile"),
    # Create. 
    path('create/', views.create_view, name="create"),
    # Update.
    path('update/<int:pk>/', views.update_view, name="update"),
    # Delete.
    path('delete/<int:pk>/', views.delete_view, name="delete"),
    
]