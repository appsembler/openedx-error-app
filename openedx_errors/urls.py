"""
URLs for openedx_errors.
"""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^barebones_django_error$', TemplateView.as_view(template_name='openedx_errors/barebones_django_error.html')),
    url(r'^barebones_mako_error$', TemplateView.as_view(template_name='openedx_errors/barebones_mako_error.html')),
    url(r'^mako_error$', TemplateView.as_view(template_name='openedx_errors/mako_error.html')),
]
