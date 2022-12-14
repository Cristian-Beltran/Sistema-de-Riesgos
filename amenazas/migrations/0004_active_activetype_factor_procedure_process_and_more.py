# Generated by Django 4.1 on 2022-08-11 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amenazas', '0003_rename_categories_categorie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ActiveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('factortype', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.active')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.IntegerField()),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.factor')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minValue', models.IntegerField()),
                ('maxValue', models.IntegerField()),
                ('detail', models.CharField(max_length=200)),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.factor')),
            ],
        ),
        migrations.CreateModel(
            name='ThreatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('activeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.activetype')),
            ],
        ),
        migrations.RemoveField(
            model_name='categoriesincident',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categoriesincident',
            name='incidence',
        ),
        migrations.RemoveField(
            model_name='good',
            name='category',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='incidenceType',
        ),
        migrations.RemoveField(
            model_name='measure',
            name='appreciation',
        ),
        migrations.DeleteModel(
            name='Risk',
        ),
        migrations.RemoveField(
            model_name='threat',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='threat',
            name='initials',
        ),
        migrations.AddField(
            model_name='threat',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='threat',
            name='confidentiality',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='threat',
            name='integrity',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='threat',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Appreciation',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='CategoriesIncident',
        ),
        migrations.DeleteModel(
            name='Good',
        ),
        migrations.DeleteModel(
            name='Incident',
        ),
        migrations.DeleteModel(
            name='IncidentsType',
        ),
        migrations.DeleteModel(
            name='Measure',
        ),
        migrations.AddField(
            model_name='active',
            name='ActiveType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amenazas.activetype'),
        ),
        migrations.AddField(
            model_name='threat',
            name='threatType',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='amenazas.threattype'),
        ),
    ]
