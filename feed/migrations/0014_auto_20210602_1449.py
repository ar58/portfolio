# Generated by Django 3.1.2 on 2021-06-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_auto_20210602_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='head_image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]