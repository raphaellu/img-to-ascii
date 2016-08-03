from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from forms import UploadImageForm
from django.http import HttpResponseRedirect
from transform_img import *
import sys


def process_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            print "success"
            img = form.cleaned_data['file']
            tf = transformImage()
            data = tf.pre_process_img(img)
            result = tf.greyscale_to_ascii(data)  # result is the ascii representation array
            display = ""
            #convert the whole array into a string to avoid re-formatting
            for row in result:
                for char in row:
                    display += char
                display += "\n"
        else:
            print "failed"
    else:
        form = UploadImageForm() 
    return render(request, 'asciiart/index.html', locals())

def index(request):
    return render(request, 'asciiart/index.html')

