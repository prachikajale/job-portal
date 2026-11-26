from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('my-jobs/',views.my_jobs,name='my_jobs'),
    path('applicants/',views.view_applicants,name='view_applicants'),
]