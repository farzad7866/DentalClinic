from urllib import request

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
        phone = request.POST.get("phone")

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
            phone=phone,
            service=service,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            message=message
        )
  
        # Email to admin
        send_mail(
            subject="New Appointment Received",
            message=f"""
            A new appointment has been booked.

            Name: {name}
            Email: {email}
            Phone: {phone}

            Service: {service}
            Date: {appointment_date}
            Time: {appointment_time}

            Message:
            {message}
            """,
            from_email=conf_settings.EMAIL_HOST_USER,
            recipient_list=[conf_settings.EMAIL_HOST_USER],
            fail_silently=True,
        )

        # Email to customer
        send_mail(
            subject="Your Appointment Has Been Booked",
            message=f"""
            Dear {name},

            Thank you for booking an appointment with PAYAM-E SEHAT DENTAL CLINIC.

            Here are your appointment details:

            Service: {service}
            Date: {appointment_date}
            Time: {appointment_time}

            If you need to change or cancel your appointment, please contact us.

            Thank you,
            PAYAM-E SEHAT DENTAL CLINIC
            """,
            from_email=conf_settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,
        )

        messages.success(
            request,
            "Your appointment has been booked successfully!"
        )

        return redirect("contact")

    return render(request, "website/contact.html")