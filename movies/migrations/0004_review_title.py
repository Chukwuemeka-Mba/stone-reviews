# Generated by Django 3.1.4 on 2021-07-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210718_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
            preserve_default=False,
        ),
    ]
