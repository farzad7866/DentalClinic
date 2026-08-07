from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "email",
        "service",
        "appointment_date",
        "appointment_time",
        "created_at",
    )

    list_filter = (
        "service",
        "appointment_date",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )

    list_editable = ("status"