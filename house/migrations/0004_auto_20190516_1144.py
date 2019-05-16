# Generated by Django 2.2.1 on 2019-05-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_auto_20190513_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(choices=[('name', 'Name lowest to highest'), ('-name', 'Name highest to lowest'), ('price', 'Price lowest to highest'), ('-price', 'Price highest to lowest'), ('size', 'Size lowest to highest'), ('-size', 'Size highest to lowest')], default='name', max_length=30)),
                ('price_low', models.IntegerField(blank=True)),
                ('price_high', models.IntegerField(blank=True)),
                ('size_low', models.IntegerField(blank=True)),
                ('size_high', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='house',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]
