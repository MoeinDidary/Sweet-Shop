from django.shortcuts import render
from django.views.generic import FormView

from contact_module.forms import ContactUSModleForm


# Create your views here.

class ContactView(FormView):
    template_name = 'contact_module/contact-us.html'
    form_class = ContactUSModleForm
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
