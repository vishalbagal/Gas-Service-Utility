from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import ServiceRequest

class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'service_request_list.html'
    context_object_name = 'requests'

class ServiceRequestCreateView(CreateView):
    model = ServiceRequest
    template_name = 'service_request_form.html'
    fields = ['description']
    success_url = '/'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)
