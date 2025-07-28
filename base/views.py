from django.shortcuts import render, HttpResponse, redirect
from base.models import Skill,Project,Experience
from portfolio.settings import ALLOWED_HOSTS
from django.contrib import messages
from base.models import Message
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Message.objects.create(name=name,email=email,message=message,ip_address=request.META.get('REMOTE_ADDR'))
        messages.success(request, 'Message sent successfully!')
        return redirect('home')
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'home/main.html',{"skills":skills,"projects":projects,"experiences":experiences})


