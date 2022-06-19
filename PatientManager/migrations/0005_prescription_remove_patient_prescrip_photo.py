# Generated by Django 4.0.4 on 2022-06-19 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PatientManager', '0004_remove_patient_patient_prescrip_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_email', models.EmailField(max_length=100)),
                ('Prescrip_Photo', models.ImageField(default='', upload_to='Prescription/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Prescrip_Photo',
        ),
    ]
