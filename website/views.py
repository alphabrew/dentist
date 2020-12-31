from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send Email
        send_mail(
        message_name, #subject
        message, #message
        message_email, #from
        ['steven.harbin@gmail.com'], # to
        fail_silently= False
        )

        return render(request, 'contact.html', {})
    else:
        #return the page
        return render(request, 'contact.html', {})
