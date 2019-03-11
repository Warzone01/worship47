from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.template import loader
from django.db.models import Q


def account(request):
    return render(request, 'account/account.html')

