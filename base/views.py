from django.shortcuts import render, HttpResponse
from base.models import Skill,Project,Experience
from portfolio.settings import ALLOWED_HOSTS
# Create your views here.
def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'home/main.html',{"skills":skills,"projects":projects,"experiences":experiences})


