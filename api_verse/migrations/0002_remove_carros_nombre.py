# Generated by Django 5.0.2 on 2024-03-02 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_verse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carros',
            name='nombre',
        ),
    ]