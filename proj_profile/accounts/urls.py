from django.urls import path, include
from accounts import views

app_name = 'accounts'
urlpatterns = [
    
    # Default URL of login.
    path('', include("django.contrib.auth.urls")),
    
    # Register.
    path('register/', views.register_view, name="register"),

]