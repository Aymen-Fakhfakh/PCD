import streamlit as st
from googletrans import Translator
import cv2
import urllib.parse
import numpy as np
import pandas as pd

def page1():
   st.set_page_config(page_title='AI Emotion Recognition Using Computer Vision in Public Spaces', layout="wide")
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
    
        st.markdown("<strong><p style='font-size:25px ;font-family:Arial'>We've trained a model named Nom_Du_Projet which can detect your clients or your own emotion. By inserting a video or an image we can give a pourcentage of every emotion wether it can be happy, sad, angry, fear, surprise, disgust or neutral to better give you information about the state of your clients.</p>", unsafe_allow_html=True)

    with DataSet:
        st.markdown("<h2 style='color: #14565A;'>Data Set</h2>", unsafe_allow_html=True)
        st.markdown("<strong><p style='font-size:25px ;font-family:Arial'>We found this data on [kaggle](http://localhost:8501) and it's called FER2013. To download it you can click [here](https://https://www.kaggle.com/datasets/msambare/fer2013) .</p>", unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
#col1,col2,col3=st.columns(3)     
#with container_2:
    #button_clicked = col2.button('(Try Nom_Du_Projet!)[]')
    #if button_clicked:
            #st.markdown('Button clicked!')

    #col1,col2,col3=st.columns(3)
     # Add a button to translate to Page 2


def page2():
     st.set_page_config(page_title="Translation", layout="wide")
# Set up the Streamlit app
st.title('AI Emotion Recognition Using Computer Vision in Public Spaces')
st.write('This app uses computer vision to analyze emotions in real-time or from video input.')

# Add support for video input
input_type = st.radio('Select input type:', ('Webcam', 'Video file'))
if input_type == 'Webcam':
    cap = cv2.VideoCapture(0,5)
else:
    video_file = st.file_uploader('Upload a video file', type=['mp4', 'avi'])
    if video_file is not None:
        file_bytes = np.asarray(bytearray(video_file.read()), dtype=np.uint8)
        cap = cv2.VideoCapture(file_bytes)
    else:
        cap = None

if cap is not None:
    # Loop over frames from the video input
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame and make an emotion prediction
       # prediction = predict_emotion(frame)

        # Display the prediction on the frame
        #cv2.putText(frame, prediction, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the frame in the Streamlit app
        st.image(frame, channels='BGR')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cap.release()

# Add user self-assessment comparison
self_assessment = st.selectbox('How are you feeling?', ['Happy', 'Sad', 'Angry', 'Neutral'])
#input_image = cv2.imread('path/to/user/input/image')
#prediction = predict_emotion(input_image)
#if prediction == self_assessment:
 #   st.write('You and the AI are in agreement!')
#else:
    #st.write('The AI predicted', prediction, 'but you feel', self_assessment)

# Add emotional state tracking
#emotional_state_data = pd.read_csv('path/to/emotional_state.csv')
#input_image = cv2.imread('path/to/user/input/image')
#prediction = predict_emotion(input_image)
#new_data = pd.DataFrame({'timestamp': pd.Timestamp.now(), 'emotion': prediction}, index=[0])
#emotional_state_data = pd.concat([emotional_state_data, new_data], ignore_index=True)
#emotional_state_data.to_csv('path/to/emotional_state.csv', index=False)
#st.line_chart(emotional_state_data.groupby(pd.Grouper(key='timestamp', freq='D')).size())

# Add social media sharing
#prediction = predict_emotion(input_image)
#twitter_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(prediction)}"
#facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote('https://example.com')}&quote={urllib.parse.quote(prediction)}"
#st.write(f'[Share on Twitter]({twitter_url})')
#st.write(f'[Share on Facebook]({facebook_url})')
    # Add a button to navigate back to Page 1

