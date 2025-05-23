# Generated by Django 5.2 on 2025-04-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_proof',
            field=models.FileField(blank=True, null=True, upload_to='payment_proofs/'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(default=1, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/'),
        ),
    ]
