# Generated by Django 5.1.4 on 2025-01-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_cartitem_order_alter_cartitem_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
