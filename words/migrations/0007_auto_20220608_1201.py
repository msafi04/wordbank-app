# Generated by Django 3.0.4 on 2022-06-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_auto_20220603_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=140, verbose_name='Author Name'),
        ),
    ]