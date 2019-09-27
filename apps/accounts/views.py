from django.shortcuts import render

from sitegate.decorators import sitegate_view

@sitegate_view  # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'entrance.html', {'title': 'Sign in & Sign up'})
