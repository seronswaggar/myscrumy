# Generated by Django 2.0.4 on 2018-04-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bayodescrumy', '0004_auto_20180429_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumyuser',
            name='role',
            field=models.CharField(choices=[('O', 'Owner'), ('A', 'Admin'), ('D', 'Developer'), ('QA', 'Quality Analyst')], default='O', max_length=50),
        ),
    ]
