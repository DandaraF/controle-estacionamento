from django.db import models


class Parking(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    plate = models.CharField(max_length=8, null=False)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    date_input = models.DateTimeField()
    date_output = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.plate


