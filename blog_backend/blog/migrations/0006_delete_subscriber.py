# Generated by Django 3.1.1 on 2020-09-23 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_subscriber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]