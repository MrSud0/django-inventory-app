# Generated by Django 4.0.3 on 2022-04-10 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_miningapp', '0004_locale_miningrig_operationcenter_overclock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='coin',
            name='live_price',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.price'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='coin',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='chip_manufacturer',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='chipset',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='core_clock',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='brand',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='height',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='length',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='model',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='noise',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='rpm',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='wattage',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='fan',
            name='width',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='comments',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='live_price',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.price'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='memory',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='memory_manufacturer',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='overclock',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.overclock'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='wattage',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.wattage'),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='coin',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.coin'),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='gpu',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.gpu'),
        ),
        migrations.AlterField(
            model_name='hashrate',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='locale',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locale',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locale',
            name='short_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='miningrig',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='miningrig',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='miningrig',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='brand',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='cpu_chip',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='core_overclock',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='core_voltage',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='memory_controller_voltage',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='memory_oveclock',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='memory_voltage',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='power_limit',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='soc_frequency',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='overclock',
            name='soc_vddmax',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='price',
            name='locale',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.locale'),
        ),
        migrations.AlterField(
            model_name='price',
            name='shop',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profitabilityexperiment',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='profitabilityexperiment',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='profitabilityforecast',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='profitabilityforecast',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='psu',
            name='efficiency',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='psu',
            name='noise',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='psu',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='psu',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='psu',
            name='wattage',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='ram',
            name='capacity',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='ram',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='ram',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='brand',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='height',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='length',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='model',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='used_in_rig',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='apps_miningapp.miningrig'),
        ),
        migrations.AlterField(
            model_name='rigcase',
            name='width',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='wattage',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='wattage',
            name='value',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
