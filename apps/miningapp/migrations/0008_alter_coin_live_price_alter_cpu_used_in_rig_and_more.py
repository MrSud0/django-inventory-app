# Generated by Django 4.0.3 on 2022-04-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_miningapp', '0007_alter_gpu_live_price_alter_gpu_overclock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='live_price',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.price'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='coin',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.coin'),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='gpu',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.gpu'),
        ),
        migrations.AlterField(
            model_name='price',
            name='locale',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.locale'),
        ),
        migrations.AlterField(
            model_name='psu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
    ]
