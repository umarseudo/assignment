import smtplib
from django.shortcuts import render,redirect
from django.contrib import messages

import uuid
# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    products = item.objects.all()
    context = {'products':products}
    return render(request, 'profile.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    products = item.objects.all()
    context = {'products':products}
    return render(request, 'profile.html', context)

def addImage(request):
    if request.method == "POST":
        prod = item()
        prod.name = request.POST.get('name')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Successfully added new image.")
        return redirect('/image')   
    return render(request,'image.html')      

def contact(request):
    if request.method == "POST":
        prod = feedback()
        prod.name = request.POST['name']
        prod.email = request.POST['email']
        prod.message = request.POST['messages']

        prod.save()
        messages.success(request, "Successfully send email")
        # token = str(uuid.uuid4())
        sender_email = "eftechdrillingsolution@gmail.com"
        rec_email = "umar.work93@gmail.com"
        password = "rbgkcfanknywqvqw"
        message = prod.message + ' ' + prod.name + ' ' + prod.email

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email, password)
        print("login success") 
        server.sendmail(sender_email, rec_email, message)
        # return render(request, "login.html")
        return redirect('/profile')
    return render(request,'contact.html')       
