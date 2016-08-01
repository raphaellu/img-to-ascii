from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, "img_site/index.html", {"message":"hello"})