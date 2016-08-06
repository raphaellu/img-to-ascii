from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
   'asciiart.views', url(r'^/$',TemplateView.as_view(
      template_name = 'asciiart/index.html')), url(r'^/success$', 'process_image', name = 'process_image'),
   url(r'^/toggle_color$', 'toggle_color', name='toggle_color')
)