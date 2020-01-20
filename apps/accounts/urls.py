from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
