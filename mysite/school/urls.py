from django.urls import path
from school import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('student/new/',views.AddStudentView.as_view(),name='add_student'),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name='student_detail'),
    path('student/<int:pk>/edit/',views.StudentUpdateView.as_view(),name='student_update'),
    path('student/<int:pk>/remove/',views.StudentRemoveView.as_view(),name='student_remove'),
    path('drafts/',views.DraftListView.as_view(),name='student_draft_list'),
    path('student/<int:pk>/publish/',views.student_publish,name='student_publish'),
    path('student/data/',views.StudentDataView.as_view(),name='student_data'),

        


]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()