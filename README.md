# EMI Personal ChatBot 💫

A **Streamlit-based chatbot** that provides warm motivational messages and interactive responses using the 
**Google Gemini API**. The app features beautiful relaxing backgrounds from Unsplash and a consistent, visually appealing interface.

---

## 🌟 Features

- **Dynamic Warm Messages**: Personalized motivational messages generated at runtime via the Gemini API.  
- **Interactive Chat**: Ask anything from your heart 💭 and get meaningful responses.  
- **Beautiful Backgrounds**: Relaxing images fetched dynamically from Unsplash API.  
- **Unified UI Colors**: All headings, chat messages, and warm messages share the same color for consistency.  
- **Persistent Background**: The background image does not fade when interacting with the chatbot.  

---

## 📦 Folder Structure

EMI_ChatBot/
│
├─ app.py # Main Streamlit app
├─ requirements.txt # Python dependencies
├─ .gitignore # Git ignore file
└─ README.md # This file

yaml
Copy code

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd EMI_ChatBot
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set your API keys

Open app.py and replace the placeholders with your own keys:

python
Copy code
GEMINI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"
UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_API_KEY"
Run the Streamlit app

bash
Copy code
streamlit run app.py
Access the app

Open the URL displayed in your terminal (usually http://localhost:8501) to interact with the chatbot.

📝 How it Works
Background Image:

Fetched from Unsplash using a set of relaxing themes.

Stored in session state to prevent fading on reruns.

Warm Message Generation:

Generated at runtime via the Gemini API.

Stored in session state for consistency.

Chat Interaction:

User input is sent to Gemini API for a response.

Chat responses are displayed with a consistent text color and semi-transparent background.

💡 Notes
The Gemini API key and Unsplash API key must be valid.

All UI elements (headings, chat messages, warm messages) use the same text color (#fefefe) for a uniform look.

If the Gemini API fails, default warm messages are displayed.

Background can optionally be refreshed periodically by modifying the code, but persistent storage prevents fading during chat input.

📌 Dependencies
streamlit

requests

google-generativeai

Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
🌐 Deployment
You can host this Streamlit app on Streamlit Cloud or any cloud provider supporting Python apps.

Steps for Streamlit Cloud:

Push your repository to GitHub.

Go to https://share.streamlit.io.

Connect your GitHub account and select this repository.


Add your Gemini and Unsplash API keys as Secrets in Streamlit Cloud for secure access.

📫 Contact
Developed by M.Umer Humayon
Email: umarhumayon0@gmail.com

