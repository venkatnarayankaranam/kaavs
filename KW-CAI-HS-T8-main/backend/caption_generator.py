import sys
import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package.strip()])

try:
    import google.generativeai as genai
    import streamlit as st
    from PIL import Image
except ImportError as e:
    print(f"Installing missing dependencies...")
    for pkg in ["google-generativeai", "streamlit", "Pillow"]:
        install_package(pkg)
    import google.generativeai as genai
    import streamlit as st
    from PIL import Image

# Configure Gemini API Key
genai.configure(api_key="AIzaSyAiUWrggrgLMFc9MOiTZOR1FhIWrlUFWN0")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_caption(uploaded_file):
    """Convert uploaded image to proper format & generate a caption."""
    try:
        # ✅ Convert UploadedFile to PIL Image
        image = Image.open(uploaded_file)

        # ✅ Generate caption using Gemini
        response = model.generate_content(["Describe this image", image])
        return response.text if response else "⚠️ Error generating caption"
    
    except Exception as e:
        return f"⚠️ Error generating caption: {str(e)}"