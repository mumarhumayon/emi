
# import streamlit as st
# import requests
# import random
# import time
# from datetime import datetime, timedelta
# import google.generativeai as genai

# # ----------------- CONFIG -----------------
# st.set_page_config(page_title="EMI's Personal ChatBox", page_icon="💫", layout="wide")

# GEMINI_API_KEY = "AIzaSyCCN3pQeIhceSHoqZKux6dD-CscoztMltI"
# UNSPLASH_ACCESS_KEY = "x9hP-tVaCBN-ZVr7x8bSDbfjksybO_2Z54e178m06oE"

# # ----------------- GEMINI SETUP -----------------
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("models/gemini-2.5-pro")

# # ----------------- SAFE AUTOREFRESH -----------------
# if not hasattr(st, "autorefresh"):
#     def autorefresh(interval=None, limit=None, key=None):
#         if "last_refresh_time" not in st.session_state:
#             st.session_state.last_refresh_time = time.time()
#         if time.time() - st.session_state.last_refresh_time > (interval / 1000):
#             st.session_state.last_refresh_time = time.time()
#             st.experimental_rerun()  # safer than os._exit
#     st.autorefresh = autorefresh

# # ----------------- BACKGROUND IMAGES -----------------
# def get_relaxing_image():
#     themes = [
#         "beautiful nature landscape",
#         "taylor swift aesthetic",
#         "BTS concert lights",
#         "calm ocean sunset",
#         "dreamy mountains",
#         "soft pink sky",
#         "peaceful forest light",
#         "calm ocean sunset",
#         "dreamy mountains",
#         "soft pink sky",
#         "peaceful forest light",
#         "gentle morning mist",
#         "lavender field at dawn",
#         "rainy window view",
#         "cozy reading nook",
#         "warm candle glow",
#         "floating lanterns",
#         "butterflies in sunlight",
#         "clouds over quiet lake",
#         "kawaii baby animals",
#         "magical forest glow",
#         "pastel watercolor landscape",
#         "floating balloons in sky",
#         "zen stone arrangement",
#         "soft autumn leaves",
#         "serene snowy path",
#         "golden wheat field"

#     ]
#     query = random.choice(themes)
#     url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("urls", {}).get("regular", None)
#         else:
#             return None
#     except:
#         return None

# if "last_bg_change" not in st.session_state or \
#    datetime.now() - st.session_state.get("last_bg_change", datetime.now()) > timedelta(minutes=2):
#     st.session_state.bg_image = get_relaxing_image()
#     st.session_state.last_bg_change = datetime.now()

# # Auto-refresh every 2 minutes to update the background
# st.autorefresh(interval=2 * 60 * 1000, limit=None, key="bg_refresh")

# # ----------------- BACKGROUND CSS -----------------
# if st.session_state.bg_image:
#     bg_url = st.session_state.bg_image
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("{bg_url}");
#             background-size: cover;
#             background-position: center;
#             transition: background-image 2s ease-in-out;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # ----------------- WARM MESSAGES -----------------
# warm_messages = [
#     "💖 You’re doing beautifully — even if it doesn’t feel like it right now.",
#     "🌅 Sometimes rest is the most productive thing you can do.",
#     "🎶 Take a breath. You’re allowed to just exist peacefully for a moment.",
#     "🌸 You are not behind — life flows at your pace.",
#     "💫 You are made of the same beauty as the sunsets and stars."
# ]



# # ----------------- CHAT UI -----------------
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown("<h2 style='color:white; text-align:center;'>🌹 EMAN's Stress Reliever</h2>", unsafe_allow_html=True)
# st.markdown(
#     f"<div style='text-align:center; font-family:Poppins; font-size:26px; color:#fefefe; text-shadow: 1px 1px 3px #000;'>{random.choice(warm_messages)}</div>",
#     unsafe_allow_html=True
# )
# user_input = st.text_input(
#     "Ask me anything from your heart 💭",
#     "",
#     placeholder="Type your thoughts here...",
#     key="chat_input",
# )

# if user_input:
#     with st.spinner("Thinking deeply... 🌙"):
#         try:
#             response = model.generate_content(user_input)
#             reply = getattr(response, "text", None) or getattr(response, "output_text", "")
#         except Exception as e:
#             reply = "⚠️ Something went wrong. Please Contact our Sir: M.Umar gmail=umarhumayon0@gmail.com"

#     st.markdown(
#         f"<div style='padding:20px; border-radius:15px; background-color:rgba(0,0,0,0.6); color:#f9f9f9; font-family:Roboto; font-size:18px;'>{reply}</div>",
#         unsafe_allow_html=True
#     )










# import streamlit as st
# import requests
# import random
# import time
# from datetime import datetime, timedelta
# import google.generativeai as genai

# # ----------------- CONFIG -----------------
# st.set_page_config(page_title="EMI's Personal ChatBox", page_icon="💫", layout="wide")

# GEMINI_API_KEY = "AIzaSyBEbX9ini0TvJZmgi5ghMsWOwiC02K8vO0"
# UNSPLASH_ACCESS_KEY = "x9hP-tVaCBN-ZVr7x8bSDbfjksybO_2Z54e178m06oE"

# # ----------------- GEMINI SETUP -----------------
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel("models/gemini-2.5-pro")

# # ----------------- SAFE AUTOREFRESH -----------------
# if not hasattr(st, "autorefresh"):
#     def autorefresh(interval=None, limit=None, key=None):
#         if "last_refresh_time" not in st.session_state:
#             st.session_state.last_refresh_time = time.time()
#         if time.time() - st.session_state.last_refresh_time > (interval / 1000):
#             st.session_state.last_refresh_time = time.time()
#             st.experimental_rerun()
#     st.autorefresh = autorefresh

# # ----------------- BACKGROUND IMAGES -----------------
# def get_relaxing_image():
#     themes = [
#         "beautiful nature landscape",
#         "taylor swift aesthetic",
#         "BTS concert lights",
#         "calm ocean sunset",
#         "dreamy mountains",
#         "soft pink sky",
#         "peaceful forest light",
#         "gentle morning mist",
#         "lavender field at dawn",
#         "rainy window view",
#         "cozy reading nook",
#         "warm candle glow",
#         "floating lanterns",
#         "butterflies in sunlight",
#         "clouds over quiet lake",
#         "kawaii baby animals",
#         "magical forest glow",
#         "pastel watercolor landscape",
#         "floating balloons in sky",
#         "zen stone arrangement",
#         "soft autumn leaves",
#         "serene snowy path",
#         "golden wheat field"
#     ]
#     query = random.choice(themes)
#     url = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             data = response.json()
#             return data.get("urls", {}).get("regular", None)
#         else:
#             return None
#     except:
#         return None

# if "last_bg_change" not in st.session_state or \
#    datetime.now() - st.session_state.get("last_bg_change", datetime.now()) > timedelta(minutes=2):
#     st.session_state.bg_image = get_relaxing_image()
#     st.session_state.last_bg_change = datetime.now()

# # Auto-refresh every 2 minutes to update the background
# st.autorefresh(interval=2 * 60 * 1000, limit=None, key="bg_refresh")

# # ----------------- BACKGROUND CSS & UNIFIED COLOR -----------------
# text_color = "#fefefe"  # color of warm message
# if st.session_state.bg_image:
#     bg_url = st.session_state.bg_image
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("{bg_url}");
#             background-size: cover;
#             background-position: center;
#             transition: background-image 2s ease-in-out;
#         }}
#         /* Make all headings and text same color */
#         h1, h2, h3, h4, h5, h6, p, div, span, label {{
#             color: {text_color} !important;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # ----------------- WARM MESSAGES -----------------
# warm_messages = [
#     "💖 You’re doing beautifully — even if it doesn’t feel like it right now.",
#     "🌅 Sometimes rest is the most productive thing you can do.",
#     "🎶 Take a breath. You’re allowed to just exist peacefully for a moment.",
#     "🌸 You are not behind — life flows at your pace.",
#     "💫 You are made of the same beauty as the sunsets and stars."
# ]

# # ----------------- CHAT UI -----------------
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown("<h2 style='text-align:center;'>🌹 EMAN's Stress Reliever</h2>", unsafe_allow_html=True)
# st.markdown(
#     f"<div style='text-align:center; font-family:Poppins; font-size:26px; text-shadow: 1px 1px 3px #000;'>{random.choice(warm_messages)}</div>",
#     unsafe_allow_html=True
# )

# user_input = st.text_input(
#     "Ask me anything from your heart 💭",
#     "",
#     placeholder="Type your thoughts here...",
#     key="chat_input",
# )

# if user_input:
#     with st.spinner("Thinking deeply... 🌙"):
#         try:
#             response = model.generate_content(user_input)
#             reply = getattr(response, "text", None) or getattr(response, "output_text", "")
#         except Exception as e:
#             reply = "⚠️ Something went wrong. Please contact M.Umar at gmail=umarhumayon0@gmail.com"
#            #  reply=e
#     st.markdown(
#         f"<div style='padding:20px; border-radius:15px; background-color:rgba(0,0,0,0.6); font-family:Roboto; font-size:18px;'>{reply}</div>",
#         unsafe_allow_html=True
#     )   





import streamlit as st
import requests
import random
from datetime import datetime
import google.generativeai as genai

# ----------------- CONFIG -----------------
st.set_page_config(page_title="EMI's Personal ChatBox", page_icon="💫", layout="wide")

GEMINI_API_KEY = "AIzaSyD8TB3g31UMia3vZP6u9pKJdY7lK8dIdhg"
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
            "Generate a short, warm, and motivational message for the user. "
            "It should be uplifting and comforting, max 1-2 sentences, include emojis if appropriate."
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
          #  reply = "⚠️ Something went wrong. Please contact M.Umar at gmail=umarhumayon0@gmail.com"
          reply=e
    st.markdown(
        f"<div style='padding:20px; border-radius:15px; background-color:rgba(0,0,0,0.6); font-family:Roboto; font-size:18px;'>{reply}</div>",
        unsafe_allow_html=True
    )

