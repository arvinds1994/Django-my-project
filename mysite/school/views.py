from django.shortcuts import render,get_object_or_404,redirect
from school.models import Teacher,Student
from school.forms import StudentForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello Pips!!!!")

class HomeView(TemplateView):
    template_name = 'school/home.html'

class AboutView(TemplateView):
    template_name = 'school/about.html'

class AddStudentView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'school/home.html'
    form_class = StudentForm

    model = Student

