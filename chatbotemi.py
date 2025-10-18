



import streamlit as st
import requests
import random
from datetime import datetime
import google.generativeai as genai

# ----------------- CONFIG -----------------
st.set_page_config(page_title="EMI's Personal ChatBox", page_icon="💫", layout="wide")

GEMINI_API_KEY = "AIzaSyCCN3pQeIhceSHoqZKux6dD-CscoztMltI"
UNSPLASH_ACCESS_KEY = "x9hP-tVaCBN-ZVr7x8bSDbfjksybO_2Z54e178m06oE"

# ----------------- GEMINI SETUP -----------------
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-pro")

# ----------------- BACKGROUND IMAGE -----------------
def get_relaxing_image():
    themes = [
        "beautiful nature landscape",
        "taylor swift aesthetic",
        "BTS concert lights",
        "calm ocean sunset",
        "dreamy mountains",
        "soft pink sky",
        "peaceful forest light",
        "gentle morning mist",
        "lavender field at dawn",
        "rainy window view",
        "cozy reading nook",
        "warm candle glow",
        "floating lanterns",
        "butterflies in sunlight",
        "clouds over quiet lake",
        "kawaii baby animals",
        "magical forest glow",
        "pastel watercolor landscape",
        "floating balloons in sky",
        "zen stone arrangement",
        "soft autumn leaves",
        "serene snowy path",
        "golden wheat field"
    ]
    query = random.choice(themes)
    url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("urls", {}).get("regular", None)
    except:
        return None

# Store background in session_state to prevent fading
if "bg_image" not in st.session_state:
    st.session_state.bg_image = get_relaxing_image()

# ----------------- BACKGROUND CSS & UNIFIED COLOR -----------------
text_color = "#fefefe"  # same color for all text
if st.session_state.bg_image:
    bg_url = st.session_state.bg_image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-position: center;
        }}
        h1, h2, h3, h4, h5, h6, p, div, span, label {{
            color: {text_color} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------- WARM MESSAGE FROM GEMINI -----------------
def get_warm_message():
    try:
        prompt = (
"""
Generate a short, gentle, and emotionally comforting message (1–2 lines max) for a 20-year-old girl who often feels sad, lonely, sick, and in grief. 
The message should sound warm, human, and kind — as if coming from a loving friend. 
It should help her feel hopeful, relaxed, and emotionally supported. 
You may include fitting emojis if they enhance comfort or positivity. 
Avoid generic advice or motivational clichés — make it soft, empathetic, and real.dpn,t ask for any option or anything, just give the expteced message
"""

            # "Generate a short, warm, and motivational message for the user. "
            # "It should be uplifting and comforting, max 1-2 sentences, include emojis if appropriate."
        )
        response = model.generate_content(prompt)
        return getattr(response, "text", None) or getattr(response, "output_text", "")
    except:
        return "💖 You’re doing beautifully — even if it doesn’t feel like it right now."

# Store warm message in session_state so it persists on reruns
if "warm_message" not in st.session_state:
    st.session_state.warm_message = get_warm_message()

# ----------------- CHAT UI -----------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>🌹 EMAN's Stress Reliever</h2>", unsafe_allow_html=True)
st.markdown(
    f"<div style='text-align:center; font-family:Poppins; font-size:26px; text-shadow: 1px 1px 3px #000;'>{st.session_state.warm_message}</div>",
    unsafe_allow_html=True
)

user_input = st.text_input(
    "Ask me anything from your heart 💭",
    "",
    placeholder="Type your thoughts here...",
    key="chat_input",
)

if user_input:
    with st.spinner("Thinking deeply... 🌙"):
        try:
            response = model.generate_content(user_input)
            reply = getattr(response, "text", None) or getattr(response, "output_text", "")
        except Exception as e:
            reply = "⚠️ Something went wrong. Please contact M.Umar at gmail=umarhumayon0@gmail.com"
          # reply=e
    st.markdown(
        f"<div style='padding:20px; border-radius:15px; background-color:rgba(0,0,0,0.6); font-family:Roboto; font-size:18px;'>{reply}</div>",
        unsafe_allow_html=True
    )






