# Generated by Django 3.2.5 on 2021-07-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0014_auto_20210706_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='htext',
            field=models.TextField(default='text', max_length=50),
        ),
    ]
