from django.shortcuts import render,redirect, get_object_or_404
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm

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
            return redirect('my_applications')
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
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'placement_portal/my_jobs.html', {'jobs': jobs})

def view_applicants(request):
    my_jobs = Job.objects.filter(posted_by=request.user)
    applications = Application.objects.filter(job__in=my_jobs)
    return render(request, 'placement_portal/view_applicants.html', {'applications': applications})
