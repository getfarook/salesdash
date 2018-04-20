from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import (View, TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class IndexView(TemplateView):
    template_name = 'netprofit/index.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'
