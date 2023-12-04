# Generated by Django 4.2.7 on 2023-11-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profil', verbose_name='Profile')),
                ('status', models.CharField(choices=[('Particulier', 'Particulier'), ('Societe', 'Societe')], max_length=30)),
                ('genre', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme'), ('Autres', 'Autres')], max_length=20)),
                ('category', models.CharField(choices=[('Grande', 'Grande'), ('Moyenne', 'Moyenne'), ('Petit', 'Petit')], max_length=20)),
                ('code_person', models.CharField(blank=True, max_length=30, verbose_name='Code person')),
                ('prenom', models.CharField(blank=True, max_length=30, null=True)),
                ('nom', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_1', models.IntegerField(blank=True, null=True)),
                ('contact_2', models.CharField(blank=True, max_length=8, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('domicile', models.CharField(blank=True, default='Lafiabougou', max_length=30, null=True)),
                ('alias', models.CharField(blank=True, max_length=30, null=True, verbose_name='alias')),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('date_naissance', models.DateField(auto_now_add=True)),
                ('nationalite', models.CharField(blank=True, max_length=30, null=True)),
                ('tutuelle', models.CharField(blank=True, max_length=30, null=True)),
                ('telephonique_fix', models.CharField(blank=True, max_length=15, null=True)),
                ('numero_reference', models.PositiveIntegerField(blank=True, null=True)),
                ('nina', models.CharField(blank=True, max_length=30, null=True)),
                ('carte_biometrique', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
