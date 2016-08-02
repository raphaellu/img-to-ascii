from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from forms import UploadImageForm
from django.http import HttpResponseRedirect
#TODO: add image handler here

def process_image(request):
	uploaded = False
	if request.method == 'POST':
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			uploaded = True
	else:
		form = UploadImageForm() 
	return render(request, 'asciiart/index.html')
	# return reverse("asciiart:process_image")

def index(request):
	return render(request, 'asciiart/index.html')

