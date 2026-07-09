from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings
from .models import Appointment

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')
        
def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request):
    return render(request, 'website/blog_details.html')

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        message = request.POST.get("message")

        # Check whether the selected date and time are already booked.
        if Appointment.objects.filter(
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists():

            messages.error(
                request,
                "Sorry, this appointment time has already been booked."
            )

            return redirect("contact")

        Appointment.objects.create(
            name=name,
            email=email,
            service=service,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            message=message
        )

        messages.success(
            request,
            "Your appointment has been booked successfully!"
        )

        return redirect("contact")

    return render(request, "website/contact.html")