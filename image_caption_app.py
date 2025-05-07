import streamlit as st
from google import genai
import tempfile

client = genai.Client(api_key="AIzaSyDLmjo9jIFXjt-cq77AEIB8kR_erm0IJVs")

# UI layout
st.title("🖼️ Image Caption Generator with Gemini")
st.write("Upload an image and select the type of description you want.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

description_type = st.selectbox(
    "Select Description Style",
    [
        "Short (1-line description)",
        "Detailed (paragraph description)",
        "Poetic (caption as a poem)"
    ]
)

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

if st.button("Generate Description"):
    if uploaded_file is not None:
        with st.spinner("Uploading image and generating description..."):
            # Save uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name

            # Upload to Gemini using temp file path
            gemini_file = client.files.upload(file=temp_file_path)

            # Prompt mapping
            prompt_map = {
                "Short (1-line description)": "Write a 1-line caption for this image.",
                "Detailed (paragraph description)": "Describe this image in detail.",
                "Poetic (caption as a poem)": "Write a short poem based on this image."
            }

            prompt = prompt_map[description_type]

            # Generate content using Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[gemini_file, prompt],
            )

            st.subheader("📃 Generated Description:")
            st.write(response.text)
    else:
        st.warning("Please upload an image before generating description.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Moosa Raza")
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