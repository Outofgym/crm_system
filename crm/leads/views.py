import re
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Lead, Agent
from .froms import LeadForm, LeadModelForm
from .models import Lead

# Create your views here.
class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'
    

class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    contexts_object_name = 'lead'
    

class LeadCreateView(generic.CreateView):
    form_class = LeadModelForm
    template_name = 'leads/lead_create.html'
    
    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadUpdateView(generic.UpdateView):
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    template_name = 'leads/lead_update.html'
    
    def get_success_url(self):
        return reverse('leads:lead_list')

class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse('leads:lead_list')

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads/')


class LandingPageView(generic.TemplateView):
    template_name='landing.html'
    