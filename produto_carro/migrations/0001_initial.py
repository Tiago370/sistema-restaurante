# Generated by Django 5.0.3 on 2024-03-29 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='produtos.produto')),
                ('cor', models.CharField(max_length=255)),
            ],
            bases=('produtos.produto',),
        ),
    ]