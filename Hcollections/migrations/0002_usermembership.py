# Generated by Django 3.2.4 on 2021-06-27 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_buyer_seller'),
        ('Hcollections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hcollections.hcollection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.buyer')),
            ],
        ),
    ]