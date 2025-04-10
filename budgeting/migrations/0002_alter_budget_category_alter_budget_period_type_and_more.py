# Generated by Django 5.1.7 on 2025-04-09 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0001_initial'),
        ('categories', '0003_alter_category_category_type'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='period_type',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly')], max_length=20),
        ),
        migrations.AlterField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
