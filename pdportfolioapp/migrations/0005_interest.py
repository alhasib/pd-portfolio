# Generated by Django 3.0.6 on 2020-07-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdportfolioapp', '0004_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]
