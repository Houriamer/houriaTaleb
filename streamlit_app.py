import streamlit 
streamlit.title('My parents New Healthy Diner houria')
streamlit.title('My parents New Healthy Diner houria')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
import pandas




import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")


