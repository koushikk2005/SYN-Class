
import streamlit as st

def header_home():

    logo_url = "src/synclass.jpeg"

    col1, col2 = st.columns(
        [1, 3],
        vertical_alignment="center"
    )

    with col1:
        st.image(logo_url, width=250)

    with col2:
        st.markdown("""
            <h1 style="
                color: #6040AE;
                font-size: 3.5rem;
                font-weight: 800;
                margin: 0;
                padding: 0;
            ">
                SYN CLASS
            </h1>
            <p style="
                color: #716783;
                font-size: 1rem;
                margin-top: -10px;
            ">
                AI Powered Attendance Management System
            </p>
        """, unsafe_allow_html=True)



def header_dashboard():
    logo_url = "src/synclass.jpeg"

    col1, col2 = st.columns([1, 4], vertical_alignment="center")

    with col1:
        st.image(logo_url, width=75)

    with col2:
        st.markdown("""
            <h2 style='color:#6040AE; margin:0;'>
                SYN CLASS
            </h2>
        """, unsafe_allow_html=True)
