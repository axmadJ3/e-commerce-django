# Generated by Django 5.1.2 on 2025-02-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderitem_options_alter_order_delivery_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('id',), 'verbose_name': 'Проданный товар', 'verbose_name_plural': 'Проданные товары'},
        ),
    ]
