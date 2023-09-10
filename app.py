# %%
import matplotlib.pyplot as plt 
import re
import json
import collections
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
import numpy as np 
from tensorflow.keras.applications.resnet50 import preprocess_input
from time import time
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.layers import *
from keras.models import *
import streamlit as st
from PIL import Image
from gtts import gTTS
import IPython.display as ipd

# %%
model=load_model('model_weights/model_19.h5')

# %%
model_temp=ResNet50(weights='imagenet',input_shape=(224,224,3))

# %%
model_resnet=Model(model_temp.input,model_temp.layers[-2].output)

# %%
def preprocess_img(img):
    img=image.load_img(img,target_size=(224,224))
    img=image.img_to_array(img)
    img=np.expand_dims(img,axis=0)

    img=preprocess_input(img)

    return img

# %%
def encode_image(img):
    img=preprocess_img(img)
    feature_vector=model_resnet.predict(img)
    feature_vector=feature_vector.reshape(1,feature_vector.shape[1])
    # print(feature_vector.shape)
    return feature_vector

# %%
with open('storage/word_to_idx.pkl','rb') as w2i:
    word_to_idx=pickle.load(w2i)
with open('storage/idx_to_word.pkl','rb') as i2w:
    idx_to_word=pickle.load(i2w)

# %%
def predict_caption(photo):
    max_len=35
    in_text = "startseq"
    for i in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence],maxlen=max_len,padding='post')
        
        ypred = model.predict([photo,sequence])
        ypred = ypred.argmax() #WOrd with max prob always - Greedy Sampling
        word = idx_to_word[ypred]
        in_text += (' ' + word)
        
        if word == "endseq":
            break
    
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption

# %%
def caption_this_image(image):
    enc=encode_image(image)
    caption=predict_caption(enc)

    return caption

#%%
def main():
    st.title("Assistive Vision CaptionBot")

    # Add a file uploader widget
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Generate and display the caption
        caption = caption_this_image(uploaded_image)
        st.write("Caption:", caption)

        tts = gTTS(text=caption, lang='en')
        tts.save("caption_audio.mp3")
        st.audio("caption_audio.mp3")

if __name__ == "__main__":
    main()
