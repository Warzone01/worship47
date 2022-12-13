from accounts.views import SignUp

from django.urls import path, include

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
