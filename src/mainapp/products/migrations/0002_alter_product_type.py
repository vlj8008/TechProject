# Generated by Django 3.2.4 on 2021-06-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizer', 'appetizer')], max_length=60),
        ),
    ]
