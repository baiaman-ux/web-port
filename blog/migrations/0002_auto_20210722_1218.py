# Generated by Django 3.2.5 on 2021-07-22 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]