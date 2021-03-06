# Generated by Django 3.1.1 on 2020-09-23 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=9)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id', 'surname', 'date'],
            },
        ),
    ]
