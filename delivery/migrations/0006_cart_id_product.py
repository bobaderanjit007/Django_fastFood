# Generated by Django 5.0 on 2023-12-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_cart_id_user_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='id_product',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
