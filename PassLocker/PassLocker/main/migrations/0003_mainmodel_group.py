# Generated by Django 4.1.4 on 2022-12-25 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('main', '0002_mainmodel_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmodel',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='groups.groupmodel'),
            preserve_default=False,
        ),
    ]
