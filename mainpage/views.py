from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Project, ContactForm, Contact
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects' : projects})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		form.save()
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'full_name': form.cleaned_data['full_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())
			recipient = 'datre63@gmail.com'
			send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
			messages.success(request, 'Success!')
			return redirect ("mainpage:index")
	form = ContactForm()
	return render(request, "pages/contact.html", {'form':form})