import streamlit as st
from  phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
import os
from pathlib import Path
import tempfile
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)


st.set_page_config(
    page_title="AI SSE Key Data Extraction",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)