# Generated by Django 4.0.2 on 2022-07-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eroomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
                ('bookid', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
