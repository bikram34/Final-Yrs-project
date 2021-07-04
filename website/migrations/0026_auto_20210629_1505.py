# Generated by Django 3.2.3 on 2021-06-29 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_alter_patients_detail_user'),
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