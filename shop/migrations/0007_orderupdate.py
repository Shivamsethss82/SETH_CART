# Generated by Django 4.1.3 on 2022-12-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
