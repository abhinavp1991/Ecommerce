# Generated by Django 3.1.6 on 2021-02-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
    ]