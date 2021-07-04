# Generated by Django 3.2.3 on 2021-06-28 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20210628_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients_detail',
            name='user',
        ),
        migrations.AddField(
            model_name='patients_detail',
            name='extendeduser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.extendeduser'),
        ),
    ]