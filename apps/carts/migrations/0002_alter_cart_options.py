# Generated by Django 5.1.2 on 2025-02-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('id',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
    ]
