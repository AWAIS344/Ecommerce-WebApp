# Generated by Django 5.1.4 on 2025-01-15 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productimage',
            name='variant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.productvariants'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
