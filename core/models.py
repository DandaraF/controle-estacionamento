from datetime import datetime

from django.db import models
from dateutil.relativedelta import relativedelta


class Parking(models.Model):
    TYPEVEHICLE = (
        ('Carro', "Carro"),
        ('Moto', 'Moto'),
        ('Caminhão', 'Caminhão'),
    )
    id = models.AutoField(primary_key=True, auto_created=True)
    client = models.CharField(max_length=255, verbose_name="Cliente")
    code = models.CharField(max_length=8, editable=False,
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

    @staticmethod
    def total_time(date_input: datetime):
        date_now = datetime.now()
        diff = abs(relativedelta(date_input, date_now))

        if diff.days > 0:
            total_hours = (diff.days * 24) + diff.hours
            return f'{total_hours} horas e {diff.minutes} minutos'

        return f'{diff.hours} horas e {diff.minutes} minutos'
