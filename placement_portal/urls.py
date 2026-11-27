from django.urls import path
from . import views
from .views import download_resume
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('my-jobs/',views.my_jobs,name='my_jobs'),
    path('applicants/', views.view_applicants, name='view_applicants'),
    path('applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('download-resume/<int:id>/',download_resume,name='download_resume'),
    path('profile/',views.profile_view,name='profile'),
]