from django.shortcuts import render, HttpResponse
from base.models import Skill,Project
# Create your views here.
def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'home/main.html',{"skills":skills,"projects":projects})


