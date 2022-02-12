import streamlit as st
import pickle
import numpy as np 



def load_model():
    loaded_model = pickle.load(open("Diabetes_prediction.pkl","rb"))
    return loaded_model


model = load_model()



st.title("Diabetes_Prediction")



Pregnancies = st.text_input('Number of Pregnancies')
Glucose = st.text_input('Glucose Level')
BloodPressure = st.text_input('Blood Pressure value')
SkinThickness = st.text_input('Skin Thickness value')
Insulin = st.text_input('Insulin Level')
BMI = st.text_input('BMI value')
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
Age = st.text_input("Age of the person")


test = st.button("Test")

if test :
    check = model.predict(np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]))

    if check[0] :
        st.text("The person is Diabetic")
    else :
        st.text("The person is not Diabetic")


