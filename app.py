import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from keras.models import load_model
import streamlit as st




start = '2010-06-22'
end = datetime.now().strftime('%Y-%m-%d')

st.title('Stock Trend Prediction')

user_input = st.text_input('Enter Stock Ticker','AAPl')
df = yf.download(user_input, start=start, end=end)
st.subheader('Data from 2010 - 2023')
st.write(df.describe())
