from accounts import views
from django.urls import include, path

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
