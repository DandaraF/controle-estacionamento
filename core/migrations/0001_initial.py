# Generated by Django 4.1.3 on 2022-12-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parking",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("client", models.CharField(max_length=255, verbose_name="Cliente")),
                (
                    "code",
                    models.CharField(
                        editable=False, max_length=8, verbose_name="Código"
                    ),
                ),
                ("plate", models.CharField(max_length=8, verbose_name="Placa")),
                ("value", models.FloatField(default=0, verbose_name="Valor")),
                ("paid", models.BooleanField(default=False, verbose_name="Pago")),
                ("left", models.BooleanField(default=False, verbose_name="Saída")),
                (
                    "vehicle",
                    models.CharField(
                        choices=[
                            ("Carro", "Carro"),
                            ("Moto", "Moto"),
                            ("Caminhão", "Caminhão"),
                        ],
                        max_length=10,
                        verbose_name="Veículo",
                    ),
                ),
                (
                    "date_input",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data entrada"
                    ),
                ),
                (
                    "date_output",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Data saída"
                    ),
                ),
            ],
        ),
    ]
