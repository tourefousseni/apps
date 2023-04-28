# Generated by Django 3.2.5 on 2023-04-27 13:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cercle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cer', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_com', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('cer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.cercle', verbose_name='Cercle')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(max_length=2)),
                ('iso2', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3)),
                ('un', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('code_parcel', models.CharField(max_length=50)),
                ('culture', models.CharField(max_length=100)),
                ('area', models.IntegerField()),
                ('perimter', models.IntegerField()),
                ('pop2005', models.IntegerField()),
                ('region', models.IntegerField()),
                ('subregion', models.IntegerField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_reg', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_vil', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.commune', verbose_name='Commune')),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.parcel')),
            ],
        ),
        migrations.AddField(
            model_name='cercle',
            name='reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.region', verbose_name='Region'),
        ),
        migrations.CreateModel(
            name='Casier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_casier', models.CharField(choices=[('Woloni', 'Woloni'), ('Tounga Ouest', 'Tounga Ouest'), ('Tounga Centre', 'Casier Centre'), ('Tounga Est', 'Casier Est'), ('Casier de Kandara', 'Casier de Kandara'), ('Tibi', 'Tibi'), ('Parampasso-NGoa', 'Parampasso-NGoa'), ('Dahelan', 'Dahelan'), ('Casier de Djenne Sud', 'Casier de Djenne Sud'), ('Casier de Djenne Nord', 'Casier de Djenne Nord'), ('Tiekilenso Nord', 'Tiekilenso Nord'), ('Tiekilenso Sud', 'Tiekilenso Sud'), ('Casier C', 'Casier C'), ('San Est I', 'San Est I'), ('San Est II', 'San Est II')], max_length=50)),
                ('culture', models.CharField(max_length=100)),
                ('locate_parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.parcel')),
            ],
        ),
    ]
