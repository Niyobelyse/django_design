# Generated by Django 4.1.1 on 2022-10-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonproject', '0003_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
