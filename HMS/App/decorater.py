from django.contrib import messages
from django.shortcuts import render , HttpResponseRedirect , redirect

def is_authenticate(function):
    def wrapper(request):
        if request.user.is_authenticated:
            messages.warning(request,'You are already login.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return function(request)
    return wrapper