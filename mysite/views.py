from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_polls(request):
    return HttpResponseRedirect(reverse('polls:index'))