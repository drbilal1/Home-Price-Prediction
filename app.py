import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open(r'C:\Users\Dell\Desktop\MS-1st Semester Data\ML Projects\House Prediction Model\House_Price_Prediction_Model.pkl','rb'))
st.header('PredictiCleaned House Price Predictor')
data = pd.read_csv(r'C:\Users\Dell\Desktop\MS-1st Semester Data\ML Projects\House Prediction Model\Cleaned_House_Price_Prediction_Dataset.csv')

loc = st.selectbox('Choose the Location', data['location'].unique())
sqft = st.number_input("Enter Total Sqft")
beds = st.number_input("Enter Total BedRooms")
bath = st.number_input("Enter Total Bathrooms")
balc = st.number_input("Enter Total Balconies")

input = pd.DataFrame([[loc,sqft,bath,balc,beds]],
                     columns=['location', 'total_sqft', 'bath', 'balcony','bedrooms'])
if st.button("Predict Price"):
    output = model.predict(input)
    out_str = "Price of the House is " + str(output[0] *100000)
    st.write(out_str)



