# Generated by Django 3.1.4 on 2020-12-11 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_title', models.CharField(max_length=100)),
                ('menu_description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('section_description', models.TextField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_sections', to='resto.menu')),
            ],
            options={
                'verbose_name': 'Menu Section',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=100)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_active', models.BooleanField()),
                ('menu_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='resto.menusection')),
            ],
            options={
                'verbose_name': 'Menu Item',
            },
        ),
    ]
