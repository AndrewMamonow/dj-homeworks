from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
   
    def __str__(self):
        return f'{self.id}, {self.name}, {self.description}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, null=True, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor.name}, {self.temperature}°C {self.created_at}'