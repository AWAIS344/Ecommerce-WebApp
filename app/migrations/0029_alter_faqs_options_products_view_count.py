# Generated by Django 5.1.4 on 2025-01-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_faqs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqs',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'fAQs'},
        ),
        migrations.AddField(
            model_name='products',
            name='view_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
