# Generated by Django 4.0.3 on 2022-05-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_wallet_accountid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_account', models.CharField(max_length=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
