# Generated by Django 4.2.2 on 2023-07-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisements_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='auction',
            field=models.BooleanField(help_text='Отметьте если торг уместен.', verbose_name='возможность торга'),
        ),
    ]