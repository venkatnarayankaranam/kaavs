import io
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get API key correctly
API_KEY = os.getenv("GEMINI_API_KEY")  # ✅ Correct usage
if not API_KEY:
    raise ValueError("❌ Gemini API key is missing! Set it in .env file.")

# ✅ Configure the API with the correct key
genai.configure(api_key=API_KEY)

# ✅ Initialize Google Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ NEW Model

def generate_story_from_image(image):
    """Generates a story based on an image using Gemini Vision."""
    try:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        # ✅ FIXED: Use `model.generate_content()`
        response = model.generate_content([
            "Describe this image and create a short story based on it.",
            img_byte_arr
        ])
        
        return response.text if response else "❌ Failed to generate story."
    except Exception as e:
        return f"Error: {str(e)}"

