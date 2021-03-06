# Generated by Django 3.0.4 on 2022-06-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20220603_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='body',
            field=models.TextField(verbose_name='Meaning'),
        ),
        migrations.AlterField(
            model_name='word',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Enter Word'),
        ),
    ]
