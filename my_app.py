"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import streamlit as st
import pandas as pd
from functions import ask_chatgpt, filter_dataframe, pd_read_csv


st.image("resources/amtsblatt_logo.png", width=200)
st.header("Eigentumsübertragungen 2020-2023")

p = r"eigentumsuebertragungen_2020-23.csv"
df =pd_read_csv(p)
df_fil = filter_dataframe(df)
st.dataframe(df_fil)

import plotly.express as px

# fig = px.scatter_mapbox(df_fil, lat="KoordinatenLat", lon="KoordinatenLon", zoom=3)
fig = px.scatter_mapbox(df_fil, hover_data=df_fil, lat=df_fil["KoordinatenLat"], lon=df_fil.KoordinatenLon, zoom=3)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

st.header("Amtsblatt")
p2 = r"kapiteltext_2020-23.csv"
# p2 = r"kapiteltext-extended_2023.csv"
df2 =pd_read_csv(p2)

df2_fil = filter_dataframe(df2)
st.dataframe(df2_fil)

question = st.text_input('ChatGPT Frage')

if st.button('Frag ChatGPT!'):
    if len(question) == 0:
        st.write("Bitte eine Frage eingeben!")
    else:
        text = df2_fil.to_string()
        if len(text)/4 > 4000:
            st.write("Auswahl zu gross!")
        else:
            # st.write(text)
            ans = ask_chatgpt(question, text)
            st.write(ans)

# df = pd.DataFrame(
#     # np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     np.expand_dims(np.array([46.87839889526367, 8.647464752197266]),0),
#     # [8.647464752197266],46.87839889526367
#     columns=['lat', 'lon'])

# st.map(df)




# st.header("Investitionen")
# text = load_txt("E:\Projects\hackdays-streamlit\input_text1.txt")
# st.write(text)

# question = st.text_input('ChatGPT Frage')

# if st.button('Frag ChatGPT!'):
#     if len(question) == 0:
#         st.write("Bitte eine Frage eingeben!")
#     else:
#         ans = ask_chatgpt(question, text)
#         st.write(ans)
