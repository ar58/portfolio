# Generated by Django 3.1.2 on 2021-06-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0029_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='web_link',
            field=models.CharField(default='https://www.', max_length=50),
        ),
    ]
