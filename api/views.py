from django.shortcuts import render

# Create your views here.
def landing(request):
	""" Landing page view """
	return render(request, 'base/landing.html')
