from django.shortcuts import render
from django.views.generic import TemplateView
from about_module.models import AboutUS


# Create your views here.

class AboutView(TemplateView):
    template_name = 'about_module/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUS.objects.all().first()
        return context
