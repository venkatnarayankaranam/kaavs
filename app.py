import streamlit as st
import streamlit.components.v1 as components
import os
import sys

# Add backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from backend.caption_generator import generate_caption
except ImportError as e:
    st.error(f"Error importing caption generator: {e}")
    sys.exit(1)

def load_html_file(filepath):
    """Load and return HTML file content"""
    try:
        # Define base directory and possible paths
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        possible_paths = [
            os.path.join(base_dir, filepath),
            os.path.join(base_dir, 'CRUD', filepath),
            filepath
        ]
        
        # Try each path
        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as file:
                    return file.read()
        
        raise FileNotFoundError(f"Could not find {filepath}")
    except Exception as e:
        st.error(f"Error loading {filepath}: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Scene Understanding",
        page_icon="🖼️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["Home", "Scene Understanding", "CRUD Interface"])
    
    with tab1:
        # Load and render index.html
        html_content = load_html_file("index.html")
        if html_content:
            components.html(html_content, height=800, scrolling=True)
        else:
            st.write("### Welcome to Scene Understanding")
            st.write("Please navigate using the tabs above.")

    with tab2:
        st.title("Scene Understanding")
        st.write("Upload an image to generate a caption")

        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Generate Caption"):
                try:
                    with st.spinner("Generating caption..."):
                        caption = generate_caption(uploaded_file)
                        st.write("### Generated Caption:")
                        st.write(caption)
                except Exception as e:
                    st.error(f"Error generating caption: {e}")

    with tab3:
        # Load and render crud.html
        crud_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crud.html")
        crud_content = load_html_file(crud_path)
        components.html(crud_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()