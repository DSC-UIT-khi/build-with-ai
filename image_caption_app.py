# Import necessary libraries
import streamlit as st                     # Streamlit for building the web interface
from google import genai                   # Google Generative AI SDK
import tempfile                            # To handle temporary file storage

# Initialize the Gemini client using your API key
# ⚠️ Important: Don't hardcode API keys in production. Use environment variables or secure storage.
client = genai.Client(api_key="your_api_key") # Replace with your actual API key this won't work

# --- Streamlit UI Setup ---

# App title and description
st.title("🖼️ Image Caption Generator with Gemini")
st.write("Upload an image and select the type of description you want.")

# File uploader widget (accepts jpg, jpeg, png files)
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Dropdown to select the style of caption
description_type = st.selectbox(
    "Select Description Style",
    [
        "Short (1-line description)",
        "Detailed (paragraph description)",
        "Poetic (caption as a poem)"
    ]
)

# If the user uploads an image, display it on the page
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# When the "Generate Description" button is clicked
if st.button("Generate Description"):
    if uploaded_file is not None:
        # Show a spinner while processing
        with st.spinner("Uploading image and generating description..."):
            
            # Save the uploaded image to a temporary file on the system
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                temp_file.write(uploaded_file.read())     # Write file content to temp file
                temp_file_path = temp_file.name           # Get file path

            # Upload the image file to Gemini
            gemini_file = client.files.upload(file=temp_file_path)

            # Map selected description type to a corresponding prompt
            prompt_map = {
                "Short (1-line description)": "Write a 1-line caption for this image.",
                "Detailed (paragraph description)": "Describe this image in detail.",
                "Poetic (caption as a poem)": "Write a short poem based on this image."
            }

            # Get the prompt based on the user's selection
            prompt = prompt_map[description_type]

            # Use the Gemini model to generate a description for the uploaded image
            response = client.models.generate_content(
                model="gemini-2.0-flash",           # Use Gemini Flash model for faster response
                contents=[gemini_file, prompt],     # Pass image + prompt as input
            )

            # Display the AI-generated caption or poem
            st.subheader("📃 Generated Description:")
            st.write(response.text)
    else:
        # If no image was uploaded, show a warning
        st.warning("Please upload an image before generating description.")

# --- Footer Section ---

# Add a horizontal rule and credit text
st.markdown("---")
st.markdown("Made with ❤️ by Moosa Raza")

# Add LinkedIn and GitHub social links with icons
st.markdown(
    """
    <div style=" padding: 10px; border-radius: 5px;">
        <a href="https://www.linkedin.com/in/syed-moosa-raza-rizvi" target="_blank" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" style="vertical-align:middle; margin-right:5px;">LinkedIn
        </a> |
        <a href="https://github.com/IamMoosa" target="_blank" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="24" style="vertical-align:middle; margin-right:5px;">GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
