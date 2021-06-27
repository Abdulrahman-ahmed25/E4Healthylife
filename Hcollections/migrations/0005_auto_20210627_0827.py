# Generated by Django 3.2.4 on 2021-06-27 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_buyer_seller'),
        ('Hcollections', '0004_alter_usermembership_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='Hcollections.hcollection'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='account.buyer'),
        ),
    ]