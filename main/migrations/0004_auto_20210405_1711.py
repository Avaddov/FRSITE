# Generated by Django 3.1.7 on 2021-04-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_gamereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamereview',
            name='first_release_date',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamereview',
            name='storyline',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamereview',
            name='summary',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamereview',
            name='url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='headline',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
