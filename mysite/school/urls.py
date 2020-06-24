from django.urls import path
from school import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('student/new/',views.AddStudentView.as_view(),name='add_student'),


]