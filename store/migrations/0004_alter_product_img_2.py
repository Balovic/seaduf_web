# Generated by Django 4.1.3 on 2022-11-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
    ]
