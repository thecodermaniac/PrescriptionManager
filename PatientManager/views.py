from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import Patient, Prescription
# Create your views here.

def index(request):
    return render(request, 'PatientManager/signup.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("patientname", "")
        email = request.POST.get("email", "")
        password=request.POST.get("psw","")
        patientInfo = Patient(Patient_name=name, Patient_email=email, Patient_password=password)
        patientInfo.save()
    
    response = redirect('/logintemp')
    return response


# global variable declare
oneuser={'oneusr':0,'PrescriptionImg':0}
logged_email={'logged':0}

def signin(request):
    return render(request, 'PatientManager/login.html')

def login(request):
    user=Patient.objects.values('Patient_email')
    if request.method== 'POST':
        for em in user:
            if em['Patient_email'] ==request.POST.get('email',""):
                print('User Found')
                logged_email['logged']=request.POST.get('email',"")
                print(logged_email['logged'])
                fulldetail=Patient.objects.filter(Patient_email=request.POST.get('email',""))
                pres_images=Prescription.objects.filter(Patient_email=request.POST.get('email',""))
                print(fulldetail)
                oneuser['oneusr']=fulldetail
                oneuser['PrescriptionImg']=pres_images
                response = redirect('/dashbrd')
                return response
                break
    else:
        return HttpResponse("Not Registered")

def dashboard(request):
    print(oneuser)
    print(logged_email['logged'])
    pres_images=Prescription.objects.filter(Patient_email=logged_email['logged'])
    oneuser['PrescriptionImg']=pres_images
    return render(request, 'PatientManager/dashboard.html',oneuser)
    pass


def AddPrescrib(request):
    if request.method== 'POST':
        id_p=logged_email['logged']
        pic=request.POST.get("picture", "")
        pres=Prescription(Patient_email=id_p,Prescrip_Photo=pic)
        pres.save()
    response = redirect('/dashbrd')
    return response