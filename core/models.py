import uuid

from django.db import models


class Parking(models.Model):
    TYPEVEHICLE = (
        ('Carro', "Carro"),
        ('Moto', 'Moto'),
        ('Caminhão', 'Caminhão'),
    )
    id = models.AutoField(primary_key=True, auto_created=True)
    client = models.CharField(max_length=255)
    # code = models.UUIDField(
    #     default=binascii.b2a_base64(os.urandom(6), newline=False),
    #     editable=False)
    code = models.UUIDField(default=uuid.uuid4(), editable=False)
    plate = models.CharField(max_length=8, null=False)
    value = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=10, choices=TYPEVEHICLE)
    date_input = models.DateTimeField(auto_now_add=True)
    date_output = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate
