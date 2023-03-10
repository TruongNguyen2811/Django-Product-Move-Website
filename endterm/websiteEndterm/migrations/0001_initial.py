# Generated by Django 4.1.3 on 2022-12-29 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('idClient', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='factory',
            fields=[
                ('idFactory', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('FactoryName', models.CharField(max_length=100)),
                ('FactoryAddress', models.CharField(max_length=250)),
                ('FactoryPhone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('idProduct', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductLine', models.CharField(choices=[('Iphone', 'Iphone'), ('Airpods', 'Airpods'), ('MacBook', 'MacBook'), ('Ipad', 'Ipad'), ('Watch', 'Watch'), ('TV&Home', 'TV&Home')], max_length=50)),
                ('Describe', models.CharField(choices=[('New', 'New'), ('Sold', 'Sold'), ('Warranting', 'Warranting'), ('Warranted', 'Warranted'), ('Cant fix', 'Cant fix'), ('Product Recall', 'Product Recall'), ('On Sale', 'On sale')], max_length=500)),
                ('idFactory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.factory')),
            ],
        ),
        migrations.CreateModel(
            name='warrantycenter',
            fields=[
                ('idWarrantyCenter', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('WarrantyCenterName', models.CharField(max_length=100)),
                ('WarrantyCenterAddress', models.CharField(max_length=250)),
                ('WarrantyCenterPhone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WarrantyDate', models.DateField()),
                ('Status', models.CharField(choices=[('Warranting', 'Warranting'), ('Cant fix', 'Cant fix'), ('Done', 'Done')], max_length=500)),
                ('Error', models.CharField(max_length=500)),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.product')),
                ('idWarrantyCenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.warrantycenter')),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('idStore', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('StoreName', models.CharField(max_length=100)),
                ('StoreAddress', models.CharField(max_length=250)),
                ('StorePhone', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SellDate', models.DateField()),
                ('WarrantyPeriod', models.DateField()),
                ('idClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.client')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.product', unique=True)),
                ('idStore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.store')),
            ],
        ),
        migrations.CreateModel(
            name='receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReceivedDate', models.DateField()),
                ('StoreWareHouse', models.CharField(max_length=250)),
                ('idFactory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.factory')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.product', unique=True)),
                ('idStore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.store')),
            ],
        ),
        migrations.CreateModel(
            name='produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfManuFacture', models.DateField()),
                ('WareHouse', models.CharField(max_length=250)),
                ('idFactory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.factory')),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteEndterm.product', unique=True)),
            ],
        ),
    ]
