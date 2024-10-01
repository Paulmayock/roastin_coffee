# Generated by Django 4.2 on 2024-10-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_bio', models.TextField()),
                ('supplier_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('supplier_website', models.TextField()),
            ],
            options={
                'verbose_name': 'Supplier',
                'db_table': 'Suppliers',
            },
        ),
    ]
