# Generated by Django 5.0.3 on 2024-04-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_rename_quantiy_orderlineitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]