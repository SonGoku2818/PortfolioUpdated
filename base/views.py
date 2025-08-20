from django.shortcuts import render, HttpResponse, redirect
from base.models import Skill,Project,Experience
from portfolio.settings import ALLOWED_HOSTS
from django.contrib import messages
from base.models import Message
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def send_email(name,email,message):
    send_mail(
        subject=f'New message from {name}',
        message=message,
        from_email=email,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        msg = Message.objects.create(name=name,email=email,message=message,ip_address=request.META.get('REMOTE_ADDR'))
        # try:
        #     send_email(name,email,message)
        #     msg.mail_sent = True
        #     msg.save()
        # except:
        #     messages.error(request, 'Failed to send message!')
        #     return redirect('home')
        messages.success(request, 'Message sent successfully!')
        return redirect('home')
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'home/main.html',{"skills":skills,"projects":projects,"experiences":experiences})


def superuser(request):
    try:
        user_obj = User.objects.create_superuser(
            username='hemant',password='123123')
        messages.success(request,'Super user has been created')
        return redirect('home')
    except Exception as e:
        messages.error(request, f'Error creating super user: {str(e)}')
        return redirect('home')