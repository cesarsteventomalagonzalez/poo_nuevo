# Generated by Django 4.1.1 on 2022-09-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuar', '0006_alter_postulante_apellidos_alter_postulante_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='usuar/media'),
        ),
    ]
