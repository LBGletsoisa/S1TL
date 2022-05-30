import urllib
import re
from bs4 import BeautifulSoup
import streamlit as st

st.set_page_config(page_title="My Website", page_icon=":tada", layout="wide")
st.subheader("Sensor 1")

st.write("Sensor 1 in the basememt tunnel, close to Grizzly section has detetected temperatures lower than the threshold of 35℃")
