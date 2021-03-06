# Generated by Django 2.1.3 on 2018-12-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lecturasensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humedad', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('momento', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='numeroentradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=100)),
                ('apellido_persona', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=9)),
                ('contrasenha', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='persona_sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainstalacion', models.DateField()),
                ('idambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ambiente')),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sensorhumedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('tipomedida', models.CharField(max_length=50)),
                ('margenerrror', models.IntegerField()),
                ('fechacompra', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='tipoconstruccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoedificacion', models.CharField(max_length=100)),
                ('densidad', models.FloatField()),
                ('area', models.FloatField()),
                ('volumen', models.FloatField()),
                ('orientacion', models.CharField(max_length=50)),
                ('materialconstruccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipoentrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=50)),
                ('altitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('msnm', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='persona_sensor',
            name='idsensorhumedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sensorhumedad'),
        ),
        migrations.AddField(
            model_name='persona_sensor',
            name='idtipoconstruccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoconstruccion'),
        ),
        migrations.AddField(
            model_name='persona_sensor',
            name='idvariable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.variables'),
        ),
        migrations.AddField(
            model_name='persona',
            name='idrol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol'),
        ),
        migrations.AddField(
            model_name='numeroentradas',
            name='idtipoconstruccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoconstruccion'),
        ),
        migrations.AddField(
            model_name='numeroentradas',
            name='idtipoentrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoentrada'),
        ),
        migrations.AddField(
            model_name='lecturasensor',
            name='idpersonasensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.persona_sensor'),
        ),
        migrations.AddField(
            model_name='lecturasensor',
            name='idsensorhumeda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sensorhumedad'),
        ),
    ]
