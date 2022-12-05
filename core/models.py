import uuid
from django.db import models


class Parking(models.Model):
    TYPEVEHICLE = (
        ('Carro', "Carro"),
        ('Moto', 'Moto'),
        ('Caminhão', 'Caminhão'),
    )
    id = models.AutoField(primary_key=True, auto_created=True)
    client = models.CharField(max_length=255, verbose_name="Cliente")
    # code = models.UUIDField(
    #     default=binascii.b2a_base64(os.urandom(6), newline=False),
    #     editable=False)
    code = models.UUIDField(default=uuid.uuid4(), editable=False,
                            verbose_name="Código")
    plate = models.CharField(max_length=8, null=False,
                             verbose_name="Placa")
    value = models.FloatField(default=0, verbose_name="Valor")
    paid = models.BooleanField(default=False, verbose_name="Pago")
    left = models.BooleanField(default=False, verbose_name="Saída")
    vehicle = models.CharField(max_length=10, choices=TYPEVEHICLE,
                               verbose_name="Veículo")
    date_input = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Data entrada")
    date_output = models.DateTimeField(null=True, blank=True,
                                       verbose_name="Data saída")

    def __str__(self):
        return self.plate
