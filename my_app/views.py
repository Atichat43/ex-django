from django.shortcuts import render
from my_app.models import Post, Comment

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

class AboutView(TemplateView):
    template_name = 'about.html'
