# Generated by Django 4.1.7 on 2024-01-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Flours', 'Flours'), ('Seeds', 'Seeds'), ('Drinks', 'Drinks'), ('Butters', 'Butters')], max_length=50),
        ),
    ]
