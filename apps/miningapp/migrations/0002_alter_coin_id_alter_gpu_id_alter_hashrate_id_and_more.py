# Generated by Django 4.0.3 on 2022-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_miningapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='id',
            field=models.BigAutoField(db_column='id', default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='id',
            field=models.BigAutoField(db_column='id', default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='id',
            field=models.BigAutoField(db_column='id', default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='id',
            field=models.BigAutoField(db_column='id', default=None, primary_key=True, serialize=False),
        ),
    ]
