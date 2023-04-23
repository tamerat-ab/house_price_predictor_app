import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import missingno as msno
import pickle

with open('train_data_features_col.pickle', 'rb') as f:
    train_data_features_col = pickle.load(f)

def correlation():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df=pd.read_csv('train.csv')
    df.columns
    plt.figure(figsize=(2, 7))
    df_corr_SalePrice = df.corr(numeric_only=True)[['SalePrice']].sort_values(by='SalePrice', ascending=False)
    df_corr_SalePrice
    x=sns.heatmap(df_corr_SalePrice, vmin=-1, vmax=1, annot=True, cmap='BrBG')
    plt.savefig('x')
    st.title('Correlation of SalePrice')
    st.pyplot()

    # return st.write('correlation',)
def visualization():
    
    with open('train_dataset.pickle','rb') as f:
        train_data= pickle.load(f) 
    Y=train_data['SalePrice']
    col_dropped=train_data.drop(['SalePrice'],axis=1)
    colns=col_dropped.columns
    cln=st.sidebar.multiselect('select feature',colns)
   
    for i in cln:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        
        st.write(f'  boxplot for{i}')
        fig = plt.figure() 
        plt.boxplot(train_data[i])
        plt.xlabel(i)
        st.pyplot(fig)
        st.write(f'saleprice vs {i}')
        fig = plt.figure() 
        # plt.stackplot(train_data[i],Y) 
        plt.scatter(train_data[i],Y)
        plt.xlabel(i)
        plt.ylabel('sale price')
        st.pyplot(fig)
