import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

st.title('Laptop Prediction Web App')
#loading the saved model
loaded_model = pickle.load(open(r"C:\Users\errav\reg.sav", 'rb'))
df = pickle.load(open(r"C:\Users\errav\final_df.sav", 'rb'))

primaryColor="#F63366"
backgroundColor="#09ab3b"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="monospace"







    #getting the input data from the user
Brand = st.selectbox('Name of Brand', df['Brand'].unique())
Processor_Name	 = st.selectbox('Processor Brand', df['Processor Name'].unique())
Processor = st.selectbox('Processor version', df['Processor'].unique())
RAM = st.selectbox('RAM' , df['RAM'].unique())
Storage1 = st.selectbox('Storage' , df['Storage1'].unique())
Generation = st.selectbox('Generation' , df['Generation'].unique())
Windows = st.selectbox('Operating System' , df['Windows'].unique())
Display1 = st.selectbox('Display size' , df['Display1'].unique())
Warranty = st.selectbox('Warranty' , df['Warranty'].unique())
new_rating = st.selectbox('Rating' , df['new_rating'].unique())

st.markdown('_ _ _ _')

button=st.button('Predict')


if button:
    df_1 = np.array([Brand,	Processor_Name,	Processor,	RAM	,Storage1,	Generation,	Windows,	Display1,	Warranty,	new_rating	])
    df_2 = df_1.reshape(1, -1)
    price=loaded_model.predict(df_2)
    st.title(int(price))
    st.balloons()
    