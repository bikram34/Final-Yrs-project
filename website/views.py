from django.shortcuts import render
from .models import doctor
from .models import extendeduser
from .models import Patients_detail
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Patients_detail, extendeduser
from django.contrib.auth import authenticate, login, logout
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import NaiveBayes


def home(request):
    return render(request, 'home.html', {})


def register(request):
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})


def edit(request):
   if request.session.get('member_id'):
        detail = User.objects.filter(id=request.user.id)
        detail2 = extendeduser.objects.filter(user_id=request.user.id)
        return render(request, 'edit.html', {"stu":detail,"stud":detail2}) 
   else:
        return HttpResponse('404 Not found')


def user_result(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            user = User.objects.get(id=request.user.id)
            user.username=username
            user.email=email
            address = request.POST['address']
            age = request.POST['age']
            dob = request.POST['dob']
            nextendeduser=extendeduser.objects.get(user_id=request.user.id)
            nextendeduser.age=age
            nextendeduser.address=address
            nextendeduser.dob=dob
            nextendeduser.save()
            user.save()
            messages.success(request, "Your account has been updated successfully")
            return redirect('update')
    else:
        return HttpResponse('404 Not found')
   



def update(request):
    if request.session.get('member_id'):
        detail = User.objects.filter(id=request.user.id)
        detail2 = extendeduser.objects.filter(user_id=request.user.id)
        detail3 = Patients_detail.objects.filter(user_id=request.user.id)
        return render(request, 'update.html', {"stu":detail,"stud":detail2,"stude":detail3}) 
    else:
        return HttpResponse('404 Not found')



def doctors(request):
    stud = doctor.objects.all()
    return render(request, 'doctor.html', {"stu":stud})


 
def about(request):
    return render(request, 'about.html', {})


def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            messages.error(request, "Username already exist")
            return redirect('register')
        except User.DoesNotExist:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username, email, password)
            address = request.POST['address']
            age = request.POST['age']
            dob = request.POST['dob']
            newextendeduser = extendeduser(address=address, age=age, dob=dob, user=user)
            newextendeduser.save()
            user.save()
            messages.success(request, "Your account has been created successfully")
            return redirect('home')
    else:
        return HttpResponse('404 Not found')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['member_id'] = username
            messages.success(request, "Login successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, please Try again.")
            return redirect('home')

    return HttpResponse('404 not found')


def user_logout(request):
    del request.session['member_id']
    auth.logout(request)
    messages.success(request, "Logout successfully.")
    return redirect('home')


def prediction(request):
    if request.session.get('member_id'):
     return render(request, 'prediction.html', {})


def result(request):
    if request.session.get('member_id'):
     l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
          'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',
          'spotting_ urination', 'fatigue',
          'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
          'patches_in_throat',
          'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration',
          'indigestion',
          'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
          'constipation',
          'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
          'fluid_overload',
          'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
          'throat_irritation',
          'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
          'fast_heart_rate',
          'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain',
          'dizziness', 'cramps',
          'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
          'brittle_nails',
          'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
          'slurred_speech', 'knee_pain', 'hip_joint_pain',
          'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements',
          'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
          'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases',
          'internal_itching', 'toxic_look_(typhos)',
          'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
          'abnormal_menstruation', 'dischromic _patches',
          'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
          'lack_of_concentration', 'visual_disturbances',
          'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
          'distention_of_abdomen', 'history_of_alcohol_consumption',
          'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking',
          'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
          'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
          'yellow_crust_ooze']

    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis',
               'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
               'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
               'Impetigo']

    l2 = []
    for x in range(0, len(l1)):
        l2.append(0)

    # TESTING DATA
    tr = pd.read_csv(r'C:\Users\Public\Testing.csv')
    tr.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    X_test = tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)

    # TRAINING DATA
    df = pd.read_csv(r'C:\Users\Public\Training.csv')

    df.replace(
        {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                       'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
                       'Hypertension ': 10,
                       'Migraine': 11, 'Cervical spondylosis': 12,
                       'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                       'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                       'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                       'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                       'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                       'Varicose veins': 30, 'Hypothyroidism': 31,
                       'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                       '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                       'Psoriasis': 39,
                       'Impetigo': 40}}, inplace=True)

    X = df[l1]

    y = df[["prognosis"]]
    np.ravel(y)

    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb = gnb.fit(X, np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    Symptom1 = request.POST['Symptom1']
    Symptom2 = request.POST['Symptom2']
    Symptom3 = request.POST['Symptom3']
    Symptom4 = request.POST['Symptom4']
    Symptom5 = request.POST['Symptom5']
    psymptoms = [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5]
    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]
    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break
    if (h == 'yes'):
      if (disease[a] == 'Fungal infection'):
         results = 'Disease Not found'
      else:
        results = disease[a]
    if(results == 'Psoriasis'):
        doctor = 'dermatologist'
    elif(results == 'Allergy' or results=='Drug Reaction' or results=='Bronchial Asthma'):
        doctor = 'Allergist'
    elif(results == 'Allergy'):
        doctor = 'Allergist'
    elif(results == 'Urinary tract infection'):
        doctor = 'urologist' 
    elif(results == 'AIDS' or results == 'Malaria' or results== 'Chicken pox' or  results== 'Dengue' or results== 'Typhoid' or results== 'Tuberculosis' or results== 'Impetigo'):
        doctor = 'Infectious Diseases' 
    elif(results == 'Hypertension' or results == 'Heartattack'):
        doctor = 'cardiologist' 
    elif(results == 'Cervical spondylosis' or results== 'Paralysis (brain hemorrhage)' or results == ' Migraine'):
        doctor = 'Neurologist'
    elif(results == 'hepatitis A' or results == 'Hepatitis B' or results== 'Hepatitis C' or results== 'Hepatitis D' or results== 'Hepatitis E'):
        doctor = 'hepatologist'
    elif(results == 'Common Cold' or results == 'Acne'):
        doctor = 'Physicians'
    elif(results == 'Pneumonia'):
        doctor = 'Pulmonologist' 
    elif(results == 'Varicoseveins'):
        doctor = 'vascular and endovascular surgeon' 
    elif(results == 'Osteoarthristis'):
        doctor = 'Orthopaedist'
    elif(results == 'Arthritis'):
        doctor = 'rheumatologist '
    elif(results == 'Diabetes ' or results == 'Hyperthyroidism' or results == 'Hypothyroidism' or results == 'Hypoglycemia'):
        doctor = 'endocrinologist'   
    elif(results == 'Chronic cholestasis' or results == 'GERD'  or results == 'Peptic ulcer diseae'  or results == 'Gastroenteritis'  or results == 'Jaundice'  or results == 'Alcoholic hepatitis'  or results == 'Dimorphic hemmorhoids(piles)'):
        doctor = 'gastroenterologist'               
    else:
     doctor = 'Doctor not found in Our database' 
    extended = User.objects.get(id=request.user.id)
    newpatients_detail = Patients_detail(Symptom1=Symptom1, Symptom2=Symptom2, Symptom3=Symptom3, Symptom4=Symptom4, Symptom5= Symptom5, suspected_Diseases= results, suggested_doctor=doctor,  user=extended)
    newpatients_detail.save()
   
   
    return render(request, 'prediction.html', {"result":results, "doctor":doctor})



    















