# Generated by Django 2.2.4 on 2019-12-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
                ('numero_siret', models.IntegerField()),
                ('adresse', models.CharField(max_length=45)),
            ],
        ),
    ]