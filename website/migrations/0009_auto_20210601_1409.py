# Generated by Django 3.2.3 on 2021-06-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210531_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='datepicker',
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='dob',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
