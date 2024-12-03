import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.markdown("""
    <style>
        /* Set background color and font family */
        body {
            background-color: #e6e6fa;  /* Lavender */
            font-family: 'Arial', sans-serif;
        }

        /* Title Styles */
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #4a90e2;
            text-align: center;
            margin-top: 20px;
        }

        /* Style input fields */
        .stNumberInput, .stTextInput {
            margin-bottom: 20px;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            border: 2px solid #4a90e2;
        }

        /* Organize input fields into 2 columns with 4 rows */
        .input-row {
            display: flex;
            justify-content: space-between;
        }

        .input-column {
            flex: 1;
            margin-right: 10px;
        }

        /* Style the Predict button with hover and active states */
        .stButton button {
            background-color: #ff9900;  /* Orange */
            color: #ffffff;  /* White */
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }

        /* Button hover effect: white text turns black when hovered */
        .stButton button:hover {
            background-color: #ff9900;  /* Keep orange background */
            color: #000000;  /* Change text to black */
        }

        /* Button active (clicked) effect: change text color to black */
        .stButton button:active {
            background-color: #ff9900;  /* Keep orange background */
            color: #000000;  /* Change text to black */
        }

        /* Style the result text */
        .result {
            font-size: 24px;
            font-weight: bold;
            color: #2ecc71;
            text-align: center;
            margin-top: 20px;
        }

        /* Style the sidebar background */
        .sidebar .sidebar-content {
            background-color: #e0e0e0;
        }
    </style>
""", unsafe_allow_html=True)
 
st.markdown('<div class="title">House Price Prediction</div>', unsafe_allow_html=True)
 
col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input('Median Income in Block Group(in $10K)', min_value=0.0)
    HouseAge = st.number_input('Median House Age in Block Group(in yrs)', min_value=0)
    AveRooms = st.number_input('Average Number of Rooms per Household', min_value=0.0)
    AveBedrms = st.number_input('Average Number of Bedrooms per Household', min_value=0.0)

with col2:
    Population = st.number_input('Block Group Population', min_value=0.0)
    AveOccup = st.number_input('Average Number of Household Members', min_value=0.0)
    Latitude = st.number_input('Block Group Latitude', min_value=-90.0, max_value=90.0)
    Longitude = st.number_input('Block Group Longitude', min_value=-180.0, max_value=180.0)
 
if st.button('Predict House Price'): 
    input_features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
     
    prediction = model.predict(input_features)

    price = prediction[0] * 10000
    
    st.markdown(f'<div class="result">Predicted House Price: ${price:,.2f}</div>', unsafe_allow_html=True)