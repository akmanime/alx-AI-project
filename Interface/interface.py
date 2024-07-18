import streamlit as st
import numpy as np
import pickle

with open('model1.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
    
st.title('Breast Tumor Diagnosis Prediction')
st.write(" Please enter clinical measurements from the biopsy to get a diagnosis prediction. ")

# fields to enter clinical measurements
radius_mean = st.number_input('Average radius')
texture_mean = st.number_input('Average texture')
perimeter_mean = st.number_input('Average perimeter')
area_mean = st.number_input('Average area')
smoothness_mean = st.number_input('Average smoothness')
compactness_mean = st.number_input('Average compactness')
concavity_mean = st.number_input('Average concavity')
concave_points_mean = st.number_input('Average concave points')
symmetry_mean = st.number_input('Average symmetry')
fractal_dimension_mean = st.number_input('Average fractal dimension')
radius_se = st.number_input('Radius SE')
texture_se = st.number_input('Texture SE')
perimeter_se = st.number_input('Perimeter SE')
area_se = st.number_input('Area SE')
smoothness_se = st.number_input('Smoothness SE')
compactness_se = st.number_input('Compactness SE')
concavity_se = st.number_input('Concavity SE')
concave_points_se = st.number_input('Concave points SE')
symmetry_se = st.number_input('Symmetry SE')
fractal_dimension_se = st.number_input('Fractal dimension SE')
radius_worst = st.number_input('Worst radius')
texture_worst = st.number_input('Worst texture')
perimeter_worst = st.number_input('Worst perimeter')
area_worst = st.number_input('Worst area')
smoothness_worst = st.number_input('Worst smoothness')
compactness_worst = st.number_input('Worst compactness')
concavity_worst = st.number_input('Worst concavity')
concave_points_worst = st.number_input('Worst concave points')
symmetry_worst = st.number_input('Worst symmetry')
fractal_dimension_worst = st.number_input('Worst fractal dimension')

# Predict Button
if st.button('Predict'):
    if (radius_mean == 0 or texture_mean == 0 or perimeter_mean == 0 or area_mean == 0 or smoothness_mean == 0):
        st.error("Please fill all the fields")
    else:
        # Feedback visuel
        with st.spinner('Prediction ...'):
            # Rassembler les mesures dans un tableau numpy
            input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                                    concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                                    radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se,
                                    concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                                    radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                                    compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
                                    fractal_dimension_worst]])

            try:
                # Faire la prédiction
                prediction = model.predict(input_data)

                # Afficher le résultat
                if prediction[0] == 1:
                    st.success("The model predicts that the tumor is malignant.")
                else:
                    st.success("The model predicts that the tumor is benign.")
            except Exception as e:
                st.error(f"An error occurred during the prediction : {str(e)}")