# from django.conf.urls import url
# from . import views


# urlpatterns = [
#     url(r'^asciiart/', views.index),
#     # url(r'^asciiart/success', 'asciiart.views.process_image', name='processImage')
# ]

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
   'asciiart.views', url(r'^asciiart/$',TemplateView.as_view(
      template_name = 'asciiart/index.html')), url(r'^asciiart/success$', 'process_image', name = 'process_image')
)