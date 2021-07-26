# Generated by Django 3.1.4 on 2021-07-26 16:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('store_number', models.CharField(max_length=20)),
                ('store_create_date', models.DateField(default=django.utils.timezone.now)),
                ('store_remake', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishes_name', models.CharField(max_length=50)),
                ('dishes_price', models.FloatField(max_length=20)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store')),
            ],
        ),
    ]
