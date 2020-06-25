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
    redirect_field_name = 'school/student_detail.html'
    form_class = StudentForm

    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentDataView(ListView):
    model = Student

    def get_queryset(self):
        return Student.objects.filter(create_date__lte=timezone.now()).order_by('id')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'school/student_detail.html'
    form_class = StudentForm

    model = Student

class StudentRemoveView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('home')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'school/student_detail.html'
    model = Student

    def get_queryset(self):
        return Student.objects.filter(create_date__isnull=True).order_by('id')

#########################################################################################

@login_required
def student_publish(request,pk):
    student = get_object_or_404(Student, pk=pk)
    student.update()
    return redirect('student_detail',pk=pk)
