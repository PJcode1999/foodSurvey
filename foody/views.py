from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.forms import UsernameField

class HomePage(TemplateView):
    template_name = "index.html"

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class AboutUS(TemplateView):
    template_name= 'About.html'

class GalleryPage(TemplateView):
    template_name= 'Gallery.html'

class ContactPage(TemplateView):
    template_name= 'Contact.html'

