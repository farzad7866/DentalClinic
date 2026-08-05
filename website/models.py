from django.db import models


# This model represents a single appointment made by a customer.
class Appointment(models.Model):

    # ==========================
    # SERVICES DROPDOWN
    # ==========================
    # These are the services the patient can choose.
    # The first value is what gets stored in the database.
    # The second value is what the user sees in the dropdown.
    SERVICE_CHOICES = [
        ("home_whitening", "Teeth Whitening Service at Home - $115"),
        ("clinic_whitening", "Teeth Whitening Service at Dental Clinic - $100"),
        ("ceramic_crown", "Ceramic Crowns and Fillings - $99"),
        ("remove_bridge", "Remove Crowns & Bridges - $50"),
        ("gum_recession", "Covering Gum Recession - $400"),
        ("consultation", "Consultation - $35"),
        ("remove_inlay", "Removal of Old Inlay/Crown - $99"),
        ("overlay_whitening", "Overlay Teeth Whitening - $170"),
        ("implant_crown", "Implant Crown - $499"),
        ("implant", "Dental Implant - $600"),
    ]


    # ==========================
    # APPOINTMENT TIME DROPDOWN
    # ==========================
    # These are the available appointment times.
    # The user can only choose one of these.
    TIME_CHOICES = [
        ("09:00", "09:00 AM"),
        ("10:00", "10:00 AM"),
        ("11:00", "11:00 AM"),
        ("12:00", "12:00 PM"),
        ("01:00", "01:00 PM"),
        ("02:00", "02:00 PM"),
        ("03:00", "03:00 PM"),
        ("04:00", "04:00 PM"),
        ("05:00", "05:00 PM"),
        ("06:00", "06:00 PM"),
        ("07:00", "07:00 PM"),
        ("08:00", "08:00 PM"),
    ]


    # ==========================
    # CUSTOMER INFORMATION
    # ==========================

    # Patient's full name.
    # Maximum length is 100 characters.
    name = models.CharField(max_length=100)

    # Patient's email address.
    # Django automatically validates that this is a valid email.
    email = models.EmailField()

    # Patient's phone number.
    phone = models.CharField(max_length=20, blank=True, null=True)

    # ==========================
    # APPOINTMENT INFORMATION
    # ==========================

    # Stores the selected service.
    # The value must be one of SERVICE_CHOICES.
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    # Stores the appointment date.
    # Example:
    # 2026-07-10
    appointment_date = models.DateField()

    # Stores the selected appointment time.
    # The value must come from TIME_CHOICES.
    appointment_time = models.CharField(
        max_length=5,
        choices=TIME_CHOICES
    )


    # ==========================
    # OPTIONAL MESSAGE
    # ==========================

    # The patient can leave extra information.
    # blank=True means this field is optional.
    message = models.TextField(blank=True)


    # ==========================
    # RECORD CREATION DATE
    # ==========================

    # Django automatically saves the date and time
    # when this appointment is first created.
    created_at = models.DateTimeField(auto_now_add=True)


    # ==========================
    # DATABASE RULES
    # ==========================
    class Meta:

        # Prevents two appointments from using
        # the same date and time.
        #
        # Allowed:
        # 10 July 2026 - 10:00 AM
        # 10 July 2026 - 11:00 AM
        #
        # Not Allowed:
        # 10 July 2026 - 10:00 AM
        # 10 July 2026 - 10:00 AM
        unique_together = ("appointment_date", "appointment_time")


    # ==========================
    # STRING REPRESENTATION
    # ==========================
    # This controls what you see in Django Admin
    # instead of "Appointment object (1)".
    def __str__(self):
        return f"{self.name} - {self.appointment_date} {self.appointment_time}"