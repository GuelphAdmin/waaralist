# Generated by Django 3.1 on 2024-03-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_memberdetails_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberdetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
