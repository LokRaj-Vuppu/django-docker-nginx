from django.shortcuts import render
from django.views.decorators.cache import cache_control

@cache_control(private=True) # The response is specific to one user and must not be cached by shared caches (like CDN, corporate proxy, ISP cache).
def homepage(request):
    return render(request, "p1.html")