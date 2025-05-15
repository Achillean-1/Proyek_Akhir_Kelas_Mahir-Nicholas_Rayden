import streamlit as st
import pandas as pd
import joblib
import numpy as np

try:
    model = joblib.load('model/dropout_rf_model_smote.pkl')
    scaler = joblib.load('model/scaler_rf.pkl')
    training_columns = joblib.load('model/training_columns.pkl')
except Exception as e:
    st.error(f"Model or scaler not found: {e}")
    st.stop()

categorical_options = {
    'Marital_status': ['single', 'married', 'divorced', 'facto union', 'legally separated', 'widower'],
    'Application_mode': ['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores)', 
                         'Holders of other higher courses', 'Admission to 2nd cycle', 'Admission to 3rd cycle', 'Other'],
    'Course': ['Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service (evening attendance)', 
               'Agronomy', 'Communication Design', 'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 
               'Management', 'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene', 'Advertising and Marketing', 
               'Journalism and Communication', 'Basic Education', 'Management (evening attendance)'],
    'Daytime_evening_attendance': ['Daytime', 'Evening'],
    'Previous_qualification': ['Secondary education', 'Higher education - bachelor', 'Higher education - degree', 
                               'Higher education - master', 'Other'],
    'Nacionality': ['Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Other'],
    'Mothers_qualification': ['Secondary Education - 12th Year', 'Higher Education - Bachelor', 'Basic Education - 9th Year', 
                              'Higher Education - Master', 'Other'],
    'Fathers_qualification': ['Secondary Education - 12th Year', 'Higher Education - Bachelor', 'Basic Education - 9th Year', 
                              'Higher Education - Master', 'Other'],
    'Mothers_occupation': ['Unskilled Workers', 'Skilled Workers', 'Administrative Staff', 'Professionals', 'Other'],
    'Fathers_occupation': ['Unskilled Workers', 'Skilled Workers', 'Administrative Staff', 'Professionals', 'Other'],
    'Displaced': ['Yes', 'No'],
    'Educational_special_needs': ['Yes', 'No'],
    'Debtor': ['Yes', 'No'],
    'Tuition_fees_up_to_date': ['Yes', 'No'],
    'Gender': ['Male', 'Female'],
    'Scholarship_holder': ['Yes', 'No'],
    'International': ['Yes', 'No']
}

numerical_features = {
    'Age_at_enrollment': (17.0, 70.0, 18.0),
    'Admission_grade': (0.0, 200.0, 100.0),
    'Previous_qualification_grade': (0.0, 200.0, 100.0),
    'Curricular_units_1st_sem_credited': (0.0, 20.0, 0.0),
    'Curricular_units_1st_sem_enrolled': (0.0, 20.0, 6.0),
    'Curricular_units_1st_sem_evaluations': (0.0, 20.0, 8.0),
    'Curricular_units_1st_sem_approved': (0.0, 20.0, 6.0),
    'Curricular_units_1st_sem_grade': (0.0, 20.0, 10.0),
    'Curricular_units_1st_sem_without_evaluations': (0.0, 20.0, 0.0),
    'Curricular_units_2nd_sem_credited': (0.0, 20.0, 0.0),
    'Curricular_units_2nd_sem_enrolled': (0.0, 20.0, 6.0),
    'Curricular_units_2nd_sem_evaluations': (0.0, 20.0, 8.0),
    'Curricular_units_2nd_sem_approved': (0.0, 20.0, 6.0),
    'Curricular_units_2nd_sem_grade': (0.0, 20.0, 10.0),
    'Curricular_units_2nd_sem_without_evaluations': (0.0, 20.0, 0.0),
    'Unemployment_rate': (0.0, 20.0, 10.0),
    'Inflation_rate': (-5.0, 10.0, 1.0),
    'GDP': (-10.0, 10.0, 0.0)
}

categorical_display_labels = {
    'Marital_status': 'Marital Status',
    'Application_mode': 'Application Mode',
    'Course': 'Course',
    'Daytime_evening_attendance': 'Daytime/Evening Attendance',
    'Previous_qualification': 'Previous Qualification',
    'Nacionality': 'Nationality',
    'Mothers_qualification': "Mother's Qualification",
    'Fathers_qualification': "Father's Qualification",
    'Mothers_occupation': "Mother's Occupation",
    'Fathers_occupation': "Father's Occupation",
    'Displaced': 'Displaced',
    'Educational_special_needs': 'Educational Special Needs',
    'Debtor': 'Debtor',
    'Tuition_fees_up_to_date': 'Tuition Fees Up to Date',
    'Gender': 'Gender',
    'Scholarship_holder': 'Scholarship Holder',
    'International': 'International'
}

numerical_display_labels = {
    'Age_at_enrollment': 'Age at Enrollment',
    'Admission_grade': 'Admission Grade',
    'Previous_qualification_grade': 'Previous Qualification Grade',
    'Curricular_units_1st_sem_credited': '1st Sem Curricular Units Credited',
    'Curricular_units_1st_sem_enrolled': '1st Sem Curricular Units Enrolled',
    'Curricular_units_1st_sem_evaluations': '1st Sem Curricular Units Evaluations',
    'Curricular_units_1st_sem_approved': '1st Sem Curricular Units Approved',
    'Curricular_units_1st_sem_grade': '1st Sem Curricular Units Grade',
    'Curricular_units_1st_sem_without_evaluations': '1st Sem Units Without Evaluations',
    'Curricular_units_2nd_sem_credited': '2nd Sem Curricular Units Credited',
    'Curricular_units_2nd_sem_enrolled': '2nd Sem Curricular Units Enrolled',
    'Curricular_units_2nd_sem_evaluations': '2nd Sem Curricular Units Evaluations',
    'Curricular_units_2nd_sem_approved': '2nd Sem Curricular Units Approved',
    'Curricular_units_2nd_sem_grade': '2nd Sem Curricular Units Grade',
    'Curricular_units_2nd_sem_without_evaluations': '2nd Sem Units Without Evaluations',
    'Unemployment_rate': 'Unemployment Rate',
    'Inflation_rate': 'Inflation Rate',
    'GDP': 'GDP'
}

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://img.freepik.com/free-vector/vector-education-logo_779267-2059.jpg", width=130)
with col2:
    st.header('Student Dropout Prediction App (Jaya Jaya Institut) :sparkles:')

data = pd.DataFrame()

st.subheader("Categorical Features")
col1, col2, col3 = st.columns(3)
categorical_inputs = {}
for i, (feature, options) in enumerate(categorical_options.items()):
    with [col1, col2, col3][i % 3]:
        value = st.selectbox(label=categorical_display_labels[feature], options=options)
        categorical_inputs[feature] = value
data = pd.DataFrame(categorical_inputs, index=[0])

st.subheader("Numerical Features")
col1, col2, col3, col4 = st.columns(4)
numerical_inputs = {}
for i, (feature, (min_val, max_val, default)) in enumerate(numerical_features.items()):
    with [col1, col2, col3, col4][i % 4]:
        value = st.number_input(
            label=numerical_display_labels[feature],
            min_value=float(min_val),
            max_value=float(max_val),
            value=float(default),
            step=0.1 if feature in ['Admission_grade', 'Previous_qualification_grade', 'Curricular_units_1st_sem_grade',
                                    'Curricular_units_2nd_sem_grade', 'Unemployment_rate', 'Inflation_rate', 'GDP'] else 1.0
        )
        numerical_inputs[feature] = value
data.update(pd.DataFrame(numerical_inputs, index=[0]))

with st.expander("View the Raw Input Data"):
    st.dataframe(data, width=800, height=200)

def preprocess_data(df):
    processed = df.copy()
    processed = pd.get_dummies(processed, columns=list(categorical_options.keys()), drop_first=True)
    for col in training_columns:
        if col not in processed.columns:
            processed[col] = 0
    processed = processed[training_columns]
    processed = scaler.transform(processed)
    return processed

if st.button('Predict'):
    try:
        X = preprocess_data(data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(pd.DataFrame(X, columns=training_columns), width=800, height=200)

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0]
        prob_df = pd.DataFrame({'Status': model.classes_, 'Probability': prob})

        st.success(f"🎓 **Predicted Student Status: {pred}**")
        st.write("🔍 **Prediction Probabilities:**")
        st.dataframe(prob_df.style.format({'Probability': '{:.2%}'}))

    except Exception as e:
        st.error(f"Error during prediction: {e}")