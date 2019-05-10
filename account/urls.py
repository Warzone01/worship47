from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    # path('accounts/login/$', LoginView.as_view(authentication_form=AuthenticationForm), name='login'),
    # path('accounts/', include('django.contrib.auth.urls')),

]