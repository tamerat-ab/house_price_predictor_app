import streamlit as st  
import requests
import json
import os
import pickle
import sys
from explore import visualization,correlation
# from features_page import dictionaries
os.environ['NO_PROXY'] = '127.0.0.1'
sys.tracebacklimit=0

st.image('image_1.jpg')
with open('numeric_dtype_features.pickle', 'rb') as f:
    numeric_features = pickle.load(f)

with open('object_dtype_features.pickle', 'rb') as f:
    object_features = pickle.load(f)


cols=[ {'object':object_features},{'int':numeric_features}]
dct={}
def features():
        s=[]
        dct={}
        x= {
            "object": st.sidebar.multiselect(
                'Select The Qualitative Data', tuple(cols[0]['object'])
            ),
            "int": st.sidebar.multiselect(
                'Select The Quantitative Data', cols[1]['int']
            )
        }

        if x['object']:
            for i in  x['object']:


                s.append(i[:3])
                for j in s:
                    if s.count(j)>1:
                        raise Exception (f'You Selected "{i}" Criterion {s.count(j)} times!!!, only one criterion is permitted')


                dct[i]=1
        else:
            dct=dct
        if x['int']:
            for i in  x['int']:
                y=st.number_input(i)
                dct[i]=y
        else:
            dct=dct
        return dct


with open('train_data_features_col.pickle', 'rb') as f:
    train_data_features_col = pickle.load(f)
dct=features()
# DICT=dct
Data={'data':dct}

if st.button("Predict"):
        try:
            response = requests.post("http://127.0.0.1:8000/upload", json=Data)
            # response = requests.post("http://0.0.0.0:8000/predict", json=data)
            #response = requests.post("http://172.18.0.3:30000/predict", json=data)
            
            prediction =response.text
            st.success(f"predicted price:{prediction}$")
            with open('api.pickle', 'rb') as f:
                df=pickle.load(f)

            st.write('Features Table',df)

        except:
           st.write('insert values')
# st.success(f"model: {prediction}")

page = st.sidebar.selectbox("Explore Or Predict", ("Acronym and description","visualization","correlation",))


if page=='visualization':
    st.title('Training Data visualization')
    visualization()
if page=='correlation':
    st.title('Training Data visualization')
    correlation()
if page == "Acronym and description":
    st.title('Acronym and description')
    with open('data_description.txt', 'r') as f:
        data_description =f.readlines()
        st.write('Click On The Arrows',data_description)