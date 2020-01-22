# Generated by Django 2.2 on 2020-01-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='desc',
        ),
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]