# Generated by Django 3.2.5 on 2021-07-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0019_remove_portfolio_member7'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='htext',
            field=models.CharField(default='Screenshot', max_length=50),
        ),
    ]