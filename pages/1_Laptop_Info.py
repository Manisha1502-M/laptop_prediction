import streamlit as st
from matplotlib import image
import os
import time
import pickle
import pandas as pd


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")




st.set_page_config(page_title="KnowAboutLaptop",
                   layout= "wide"
)
st.title("About Laptop")



data_path = os.path.join(dir_of_interest, "data", "df.pkl")

lap = pickle.load(open(data_path, 'rb'))

df = pd.DataFrame(lap)

laptop = df["Product"].values
index = df["Product"].index
st.subheader("Information About Some of Laptop Model")
selected_laptop_name = st.selectbox("select the model:- ", laptop)
butt = st.button("Okay")
if butt:
    info = df.loc[df['Product'] == selected_laptop_name]
    st.write(info.iloc[0])
    
















