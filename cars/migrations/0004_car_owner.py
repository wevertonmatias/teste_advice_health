# Generated by Django 4.1.3 on 2022-11-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_alter_owner_cpf_alter_owner_name_and_more'),
        ('cars', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='owners.owner'),
        ),
    ]
