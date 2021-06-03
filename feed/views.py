from django.core.checks import messages
from django.shortcuts import render
from .models import Footer, Intro,About, Skill, Work, Footer, Contact
from django.views.generic import TemplateView,FormView
from .forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context             = super().get_context_data(**kwargs)
        context["intros"]   = Intro.objects.all()
        context["abouts"]   = About.objects.all()
        context["skills"]   = Skill.objects.all()
        context['works']    = Work.objects.all().order_by('-id')
        context['foot']     = Footer.objects.all()
        return context
    
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def form_valid(self, form):
        
        new_object = Contact.objects.create(
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            message =form.cleaned_data['message']
        )
        return super().form_valid(form)
