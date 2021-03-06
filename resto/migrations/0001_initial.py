# Generated by Django 3.1.4 on 2021-01-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item_name', models.CharField(max_length=100)),
                ('menu_item_description', models.TextField(blank=True, null=True)),
                ('menu_item_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Menu Item',
            },
        ),
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_section_name', models.CharField(max_length=25, null=True)),
                ('menu_section_alias', models.CharField(max_length=25, null=True)),
                ('menu_items', models.ManyToManyField(blank=True, null=True, to='resto.MenuItem')),
            ],
            options={
                'verbose_name_plural': 'Menu Section',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=25, null=True)),
                ('menu_section_name', models.ManyToManyField(blank=True, null=True, to='resto.MenuSection')),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
    ]
