import google.generativeai as genai
import PIL.Image

# Configure Google Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your actual API key

def get_image_caption(image_file):
    """Generates a caption for an uploaded image using Google Gemini Vision API."""
    try:
        image = PIL.Image.open(image_file)
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content([image])
        return response.text  # Extract caption text
    except Exception as e:
        return f"Error generating caption: {e}"
