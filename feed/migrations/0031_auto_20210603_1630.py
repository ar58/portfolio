# Generated by Django 3.1.2 on 2021-06-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0030_work_web_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='web_link',
            field=models.CharField(default='https://www.', max_length=50, null=True),
        ),
    ]
