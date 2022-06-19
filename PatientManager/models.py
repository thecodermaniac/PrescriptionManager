from django.db import models

# Create your models here.

class Prescription(models.Model):
    Patient_email=models.EmailField(max_length=100)
    Prescrip_Photo=models.ImageField(upload_to="Prescription/images",default='') 

class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    Patient_name=models.CharField(max_length=100)
    Patient_email=models.EmailField(max_length=100)
    Patient_password=models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.Patient_name

