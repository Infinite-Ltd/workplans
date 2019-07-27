# Generated by Django 2.0.7 on 2018-07-18 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_workplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='dirLeader',
            field=models.CharField(default='陈清洲', max_length=20),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='isleader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workplan',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Userinfo'),
            preserve_default=False,
        ),
    ]