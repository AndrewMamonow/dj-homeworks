from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    list_display = ['__str__']