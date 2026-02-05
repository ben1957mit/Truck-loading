import streamlit as st
from utils.trailer_data import TRAILERS

st.title("Trailer Comparison")

for name, t in TRAILERS.items():
    st.subheader(name)
    st.write(f"Length: {t['length']} ft")
    st.write(f"Width: {t['width']} ft")
    st.write(f"Height: {t['height']} ft")
    st.write(f"Max Weight: {t['max_weight']} lbs")
