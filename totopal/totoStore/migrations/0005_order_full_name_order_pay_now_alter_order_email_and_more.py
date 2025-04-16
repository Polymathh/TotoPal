# Generated by Django 5.1.7 on 2025-04-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totoStore', '0004_order_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_now',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
