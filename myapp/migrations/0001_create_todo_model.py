# Generated by Django 3.2.8 on 2021-10-31 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
