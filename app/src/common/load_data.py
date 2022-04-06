import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_dataset():
    df = pd.read_csv('./data/chocolate.csv')
    df.drop(columns=['Unnamed: 0','ref','beans','specific_bean_origin_or_bar_name','cocoa_butter','vanilla','lecithin','salt','sugar','sweetener_without_sugar','first_taste','second_taste','third_taste','fourth_taste'],inplace=True)
    conditions = [
                    (df['rating'] >= 4.0) & (df['rating'] <= 5.0),
                    (df['rating'] >= 3.5) & (df['rating'] <= 3.9),
                    (df['rating'] >= 3.0) & (df['rating'] <= 3.49),
                    (df['rating'] >= 2.0) & (df['rating'] <= 2.9),   
                    (df['rating'] >= 1.0) & (df['rating'] <= 1.9),         
    ]
    values = ['Outstanding','Highly Reccomended','Reccomended','Disappointing','Unpleasant']
    df['rating_value'] = np.select(conditions, values)
    return df