# Generated by Django 3.0.8 on 2020-09-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_app', '0003_dog_toys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='L', max_length=1),
        ),
    ]
