from django.shortcuts import render
from django.views.generic import TemplateView

from product_module.models import ProductCategory


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/home-site.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
