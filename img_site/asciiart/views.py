from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from forms import UploadImageForm
from django.http import HttpResponseRedirect
from transform_img import *
import sys


def toggle_color(request):
    if request.session["color"] == "white":
        request.session['display'] = request.session["display_black"]
        request.session["color"] = "black"
    else:
        request.session['display'] = request.session["display_white"]
        request.session["color"] = "white"
    # return render(request, 'asciiart/success.html')
    return HttpResponse(request.session['display'])

def process_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['file']
            tf = transformImage()
            data = tf.pre_process_img(img)
            results = tf.greyscale_to_ascii(data)  # results contain result_white and result_black
            display_white = "\n"
            display_black = "\n"
            #convert the whole array into a string to avoid re-formatting
            for row in results[0]:  # result_white
                for char in row:
                    display_white += char
                display_white += "\n"
            request.session["display_white"] = display_white  # store display_white into request session

            for row in results[1]:  # result_black
                for char in row:
                    display_black += char
                display_black += "\n"
            request.session["display_black"] = display_black # store display_black into request session

            request.session['display'] = display_white  # by default, display white ascii art
            request.session["color"] = "white"
        else:
            print "uploading image failed"
    else:
        form = UploadImageForm() 
    return render(request, 'asciiart/success.html')

def index(request):
    return render(request, 'asciiart/index.html')

