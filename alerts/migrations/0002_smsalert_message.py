# Generated by Django 2.0.2 on 2018-03-10 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsalert',
            name='message',
            field=models.TextField(default="Don't forget to continue reading"),
        ),
    ]