# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:07:00 2025

@author: Dell
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_data=pickle.load(open('diabetes_model.sav','rb'))

heart_data=pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_data=pickle.load(open('parkinsons_model.sav','rb'))


with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)


if(selected=='Diabetes Prediction'):
    st.title("Diabetes Prediction usnig ML")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
        
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        
        user_input = [float(x) for x in user_input]
        
        diab_prediction = diabetes_data.predict([user_input])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
            
    st.success(diab_diagnosis)

    
if(selected=='Heart Disease Prediction'):
    st.title("Heart Disease Prediction usnig ML")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        sex = st.text_input('Sex (1 = male, 0 = female)')
        cp = st.text_input('Chest Pain types (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptotic)')
        trestbps = st.text_input('Resting Blood Pressure in mmHg')
        
        
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = yes, 0 = no)')
        restecg = st.text_input('Resting Electrocardiographic results (0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy)')
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)')
        oldpeak = st.text_input('ST depression induced by exercise')
        slope = st.text_input('Slope of the peak exercise ST segment (0 = upsloping, 1 = flat, 2 = downsloping)')
        ca = st.text_input('Major vessels (0–4) colored by fluoroscopy')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
             
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        user_input = [float(x) for x in user_input]
        
        heart_prediction = heart_data.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.markdown("---") 
          
    st.success(heart_diagnosis)


if(selected=="Parkinsons Prediction"):
    st.title("Parkinsons Prediction using ML")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Fo=st.text_input('MDVP:Flo(Hz) Average vocal fundamental frequency')
    with col2:
        Fhi=st.text_input('MDVP:Flo(Hz) Maximum vocal fundamental frequency')
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz) Minimum vocal fundamental frequency')
        
    with col1:
        Jitter=st.text_input('Jitter:DDP Measures of variation in fundamental frequency')
        
    with col2:
        spread1=st.text_input('spread1')
        
    with col3:
        spread2=st.text_input('spread2')
    
    with col1:
        PPE=st.text_input('PPE')
    
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        user_input = [Fo,Fhi,Flo,Jitter,spread1,spread2,PPE]
        
        user_input = [float(x) for x in user_input]
        
        parkinsons_prediction = parkinsons_data.predict([user_input])
    
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
    
    
