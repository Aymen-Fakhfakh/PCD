import os
import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.events import DoubleTap 
from PIL import Image

st.set_page_config(page_title="Emotional recognitation", layout="wide")
container_1=st.container()
container_2=st.container()
header=st.container()
introduction=st.container()
DataSet=st.container()
model=st.container()

nav_container = st.container()





with container_1:
    with header:
        st.title('Emotional recognitation Website')

    with introduction:
        st.markdown("<h2 style='color: #14565A;'>Introducing Nom_Du_Projet</h2>", unsafe_allow_html=True)
    
        st.markdown("<strong><p style='font-size:35px ;font-family:Arial'>We've trained a model named Nom_Du_Projet which can detect your clients or your own emotion. By inserting a video or an image we can give a pourcentage of every emotion wether it can be happy, sad, angry, fear, surprise, disgust or neutral to better give you information about the state of your clients.</p>", unsafe_allow_html=True)

   # with DataSet:
    #    st.markdown("<h2 style='color: #14565A;'>Data Set</h2>", unsafe_allow_html=True)
     #   st.markdown("<strong><p style='font-size:25px ;font-family:Arial'>We found this data on [kaggle](http://localhost:8501) and it's called FER2013. To download it you can click [here](https://https://www.kaggle.com/datasets/msambare/fer2013) .</p>", unsafe_allow_html=True)
      #  st.write('')
       # st.write('')
        #st.write('')
#col1,col2,col3=st.columns(3)     
#with container_2:
  #  button_clicked = col2.button('(Try Nom_Du_Projet!)[]')
   # if button_clicked:
    #        st.markdown('Button clicked!')

    #col1,col2,col3=st.columns(3)
    #image = Image.open('Giyu.jpg')
    #col1.image(image, caption='Mah boy')

def authenticate(username, password):
    # Replace with your own authentication logic
    if username == "user" and password == "password":
        return True
    else:
        return False

def main():
    
    # Get user credentials
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Authenticate user
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            # Add your code to redirect to another page here
        else:
            st.error("Incorrect username or password")

if __name__ == "__main__":
    main()







    
    
    
    