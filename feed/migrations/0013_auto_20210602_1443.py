# Generated by Django 3.1.2 on 2021-06-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_auto_20210602_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]