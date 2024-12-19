# Generated by Django 4.2 on 2024-12-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "query",
                    models.CharField(
                        choices=[
                            ("ORDER QUERY", "ORDER QUERY"),
                            ("PAYMENT ISSUE", "PAYMENT ISSUE"),
                            ("LOGIN ISSUE", "LOGIN ISSUE"),
                            ("GENERAL QUERY", "GENERAL QUERY"),
                        ],
                        default="GENERAL QUERY",
                        max_length=40,
                    ),
                ),
                ("comments", models.CharField(max_length=2000)),
            ],
        ),
    ]
