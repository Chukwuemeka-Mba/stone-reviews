# Generated by Django 3.1.4 on 2021-07-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]