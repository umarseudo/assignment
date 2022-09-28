# Generated by Django 4.1.1 on 2022-09-20 07:08

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to=myapp.models.filepath)),
            ],
        ),
    ]
