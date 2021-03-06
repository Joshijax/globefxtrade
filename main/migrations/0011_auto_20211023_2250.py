# Generated by Django 3.2.8 on 2021-10-23 21:50

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211022_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='btc_balance',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0001'), default_currency='USD', max_digits=14),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='eth_balance',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0001'), default_currency='USD', max_digits=14),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='usdt_balance',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0.0001'), default_currency='USD', max_digits=14),
        ),
    ]
