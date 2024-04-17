import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import requests

import plotly.graph_objs as go
import numpy as np
from PIL import Image


# Path to your header image
header_path = "productBreakdown.jpg"

# Display the header image
st.image(header_path, use_column_width=True)

# Function to load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Define the URLs of your images
image_url1 = "SWOTAnalysis.jpg"
image_url2 = "roadmap1.jpg"
image_url3 = "roadmap2.jpg"

# Load the Lottie animations
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
spreadhseet_lottie = load_lottieurl("https://lottie.host/2429370d-89e5-4e65-bdca-d1cb9b1e904b/OkX4reeuxC.json")
ar_lottie = load_lottieurl("https://lottie.host/e6e6d774-662d-43d7-ab12-7b7f0a24c2e8/JvqlAlnX6i.json")
sr_lottie = load_lottieurl("https://lottie.host/2d360ef5-d543-4514-8405-6fef02b5efb4/JvRIXZkfrs.json")
voice_lottie = load_lottieurl("https://lottie.host/d1d713d6-2453-4647-8c28-80a9d71d26d2/co4X4BkWH0.json")
audiobook_lottie = load_lottieurl("https://lottie.host/175f03cf-ccb2-46c8-9c84-6bc4dda79b1a/NZvmVkK9VY.json")
ocr_lottie = load_lottieurl("https://lottie.host/bb18a4dd-7b4f-4ac8-a86f-e8286155a776/F0zyPvD4Fj.json")
llm_model = load_lottieurl("https://lottie.host/b4edcf13-0c11-40ef-b954-899f9375cb70/nZ3xL0caa1.json")
cloud_lottie = load_lottieurl("https://lottie.host/500e4373-59b7-4831-9f73-48bf2f211300/Qb5E7j6E0F.json")

# Define the list of Lottie animation URLs for each skill
lotties = [python_lottie, docker_lottie, github_lottie, figma_lottie, spreadhseet_lottie, ar_lottie, sr_lottie, voice_lottie, audiobook_lottie, ocr_lottie, llm_model, cloud_lottie]

# Define the number of columns based on the screen width
num_columns = min(len(lotties), 4)  # Maximum 4 columns

# Center-align the toolkit subheader and ensure responsiveness
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- skillset ----------------- #
with st.container():
    # Set up the Streamlit layout
    st.markdown("""
        <div style='text-align: center;'>
        <br>
            <h2>🧰 Toolkit</h2>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

    # Display the Lottie animations in the columns
    cols = st.columns(num_columns)
    for i, lottie in enumerate(lotties):
        with cols[i % num_columns]:
            st_lottie(lottie, height=100, width="100%", key=lottie, speed=2.5)

# Add a horizontal line
st.markdown("<hr/>", unsafe_allow_html=True)

# Center-align the SWOT Analysis subheader and ensure responsiveness
st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px; /* Add some padding for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the SWOT Analysis image
st.image(image_url1, use_column_width=True)

# Add a horizontal line
st.markdown("<hr/>", unsafe_allow_html=True)

# Display the Roadmap images
st.image(image_url2, use_column_width=True)
st.image(image_url3, use_column_width=True)

# Add a horizontal line
st.markdown("<hr/>", unsafe_allow_html=True)

# Add the footer
st.markdown("""
    <footer style="text-align: center; background-color: #8A2BE2; color: #ffffff; padding: 10px;">
        Prosync.AI - Your Career Advisory Partner
    </footer>
""", unsafe_allow_html=True)
