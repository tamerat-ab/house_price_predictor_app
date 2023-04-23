import numpy as np
from typing import List,Dict,Optional
import pandas as pd
import json
import os
from sklearn import preprocessing
# os.environ['NO_PROXY'] = '127.0.0.1'
import pickle
from fastapi import FastAPI
from typing import Dict, Set, Union
from pydantic import BaseModel, Field
from typing import Literal
import uvicorn

app = FastAPI()
class Data(BaseModel):
    data:dict
   


with open('train_data_features_col.pickle', 'rb') as f:
    train_data_features_col = pickle.load(f)

@app.post("/upload")
async def upload(DIC: Data):

    dct_1=DIC.data
    dct_2={}
    dict_kyes_list=list(dct_1.keys())
    set_dict = set(dict_kyes_list)
    set_col = set(train_data_features_col)
    diff_col=set_col.difference(set_dict)
    diff_col=list(diff_col)
    for j in diff_col:
        dct_2[j]=0
    dct_2
    merged_dict= {**dct_1,**dct_2}
    df=pd.DataFrame([merged_dict])
    df=df[train_data_features_col]
    df
    with open('api.pickle', 'wb') as f:
        pickle.dump(df, f)


    col_higher_magnitude=[]
    col_lower_magnitude=[]
    col=df.columns
    for i in col:
        if any(df[i]>10):
            col_higher_magnitude.append(i)
        else:
            col_lower_magnitude.append(i)
    col_higher_magnitude
    col_lower_magnitude

    with open('GradientBoostingRegressor.pickle', 'rb') as f:
        model = pickle.load(f)
    try:
        min_max_scaler = preprocessing.MinMaxScaler(feature_range =(0, 1))
        min_max_scaler_after = min_max_scaler.fit_transform(df[col_higher_magnitude])
        df_higher=pd.DataFrame(min_max_scaler_after,columns=col_higher_magnitude)
        df=pd.concat([df_higher,df[col_lower_magnitude]],axis=1)
        df=df[train_data_features_col]
        df_pred=model.predict(df)

        return   round(df_pred[0],2)
    except:
        return 'Please Insert At lest one value for both Numeric and Object Datatype'


if __name__=='__main__':
    uvicorn.run (app , host= '127.0.0.1')

    # uvicorn.run (app, host= 'localhost', port=600)

























# import streamlit
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import plotly.express as px
# import matplotlib.pyplot as plt
# from sklearn import preprocessing, svm
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import missingno as msno 
# from fastapi import FastAPI
# import uvicorn
# from model import Data

# app = FastAPI()

# @app.get("/")
# def show_1():
#     return {"Hello": "this is a test"}
# @app.post("/predict")
# def predict(data:model):
#     return {'test': data}



# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=500)
