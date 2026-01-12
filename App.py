
"""
Created on Mon Jan 12 10:40:52 2026

@author: gajan
"""
# imports

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np


# Title and Subheader
st.title('Exploratory Data Analysis')
st.subheader('Data Anlysis Web fApp using Python & Stremlit')

# Upload Data Set File
upload = st.file_uploader('Upload your Dataset (In CSV File) ')
if upload is not None:
    data = pd.read_csv(upload)

# Check uploaded dataset
if upload is not None:
    if st.checkbox('Preview of Dataset'):
        if st.button('Top 5 Rows'):
            st.write(data.head())
        if st.button('5 Random Rows'):
            st.write(data.sample(5))
        if st.button('Last 5 Rows'):
            st.write(data.tail())
            
# Check Data Type & anfo of Each column
if upload is not None:
    if st.checkbox('Metadata of Data'):
        data_shape=st.radio('Check size of Rows and Columns',('Rows','Columns'))
        if data_shape=='Rows':
            st.text('Number of Rows') 
            st.write(data.shape[0])
        if data_shape=='Columns':
            st.text('Number of Columns')
            st.write(data.shape[1])
            
        if st.button('Print all Columns'):
            st.write(data.columns)
        if st.button('Datatypes of dataset'):
            st.write(data.dtypes)
        if st.button('Summary of the Dataset'):
            st.write(data.describe(include='all'))

# Find Null values in the dateset
if upload is not None:
    if st.checkbox('Check Null Values in Dataset'):
        test=data.isnull().values.any()
        if test == True:
            if st.warning('There are Null values in Dataset'):
                sns.heatmap(data.isnull())
                st.pyplot()
        else: 
            st.success('Congrass! No missing Values..')

# Check for Duplicate Values
if upload is not None:  
    if st.checkbox('Check Duplicate Data in Dataset'):
        test= data.duplicated().any()
        if test == True:
            st.warning('This Dataset Contain some duplicate Values!')
            dup = st.selectbox('Do you want to remove duplicates form dataset?',('Select one','Yes','No'))
            if dup == 'Yes':
                data = data.drop_duplicates()
                st.success('Duplicate Values are Removed')
            if dup == 'No':
                st.text('OK! No Problem..')
        else:
            st.success('Good! No Duplicates..')
# Download dataset after eda
    csv_data = data.to_csv(index=False)
    
    st.download_button(
        label="📥 Download EDA Data",
        data=csv_data,
        file_name="eda_processed_data.csv",
        mime="text/csv"
    )
            

                
            
# About section 
if st.button('About App'):
    st.text("""
            This web application is built using Streamlit to perform Exploratory Data Analysis (EDA) in an interactive and user-friendly way. The goal of the app is to help users quickly understand the structure, quality, and patterns in a dataset without writing complex code.
            The app allows users to upload datasets and explore them through summary statistics, data previews, missing value analysis, and visualizations. 

This application is especially useful for:
1. Data analysts during initial data exploration
2. Students learning data analysis concepts
3. Anyone who wants quick insights from raw data
The app is designed to be simple, fast, and intuitive, making EDA more accessible and efficient.
                       Thank You!!! """)
        
# By
if st.checkbox('By'):
    st.success('Gajanan Ghuge')
    
    
