from django.shortcuts import render,redirect, get_object_or_404
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from django.http import FileResponse, Http404
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.student = request.user
            app.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'placement_portal/apply_job.html', {'form': form, 'job': job})

@login_required
def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            description=request.POST.get('description'),
            package=request.POST.get('package'),
            location=request.POST.get('location'),
            deadline=request.POST.get('deadline'),
            posted_by=request.user
        )
        return redirect('home')
    return render(request, 'accounts/post_job.html')

def my_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'placement_portal/my_jobs.html', {'jobs': jobs})

def view_applicants(request, job_id=None):
    if job_id:
        applications = Application.objects.filter(job_id=job_id)
    else:
        applications = Application.objects.all()
    return render(request, 'placement_portal/view_applicants.html', {'applications': applications})

def download_resume(request, id):
    app = Application.objects.get(id=id)
    if not app.resume or not os.path.exists(app.resume.path):
        raise Http404("Resume file not found")
    return FileResponse(open(app.resume.path, 'rb'), as_attachment=True, filename=os.path.basename(app.resume.path))

def post_job(request):
    return render(request, 'post_job.html')

def view_applications(request):
    return HttpResponse("<h1>View Applications Page</h1><a href='/accounts/dashboard/'>Back to Dashboard</a>")

def view_jobs(request):
    return HttpResponse("<h1>View All Jobs Page</h1><a href='/accounts/dashboard/'>Back to Dashboard</a>")

@login_required
def profile_view(request):
    return render(request,'accounts/profile.html')

def csrf_failure(request, reason=""):
    from django.contrib import messages
    messages.error(request, "Session expire zali, parat login kara!")
    return redirect('login')