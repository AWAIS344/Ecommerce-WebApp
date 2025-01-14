# Generated by Django 5.1.4 on 2025-01-14 06:53

from django.db import migrations, models
from django.utils.timezone import now



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_order_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]