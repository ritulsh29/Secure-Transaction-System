# Generated by Django 4.2.2 on 2024-03-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder', models.CharField(max_length=20)),
                ('routing_number', models.CharField(max_length=5)),
                ('account_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Creditmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_on_card', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=20)),
                ('expiry_mm', models.CharField(max_length=5)),
                ('cvv', models.CharField(max_length=5)),
            ],
        ),
    ]
