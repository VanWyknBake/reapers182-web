# Generated by Django 3.2.5 on 2021-07-03 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0004_portfolio_htext'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='htext',
            field=models.CharField(default='text', max_length=50),
        ),
    ]
