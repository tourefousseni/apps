# Generated by Django 3.2.5 on 2023-05-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalaliso', '0002_alter_mesure_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_paypal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
