# 🖼️ Image Caption Generator with Gemini

A Streamlit web application that generates captions for uploaded images using Google's Gemini AI model.

## Features

- Upload images in JPG, JPEG, or PNG format
- Choose from three description styles:
  - Short (1-line description)
  - Detailed (paragraph description)
  - Poetic (caption as a poem)
- Instant AI-powered image descriptions
- Simple and intuitive user interface

## Prerequisites

Before running this application, you'll need:

- Python 3.7+
- A Google AI Studio API key (Gemini API)
- Obtain a Google AI Studio API key from [here](https://aistudio.google.com/apikey)

## Installation

1. Clone this repository or download the source code:

```bash
git clone https://github.com/DSC-UIT-khi/build-with-ai.git
cd build-with-ai
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Replace the API key in the code with your own Google AI Studio API key:

```python
client = genai.Client(api_key="YOUR_API_KEY_HERE")
```

**Important**: It's recommended to use environment variables for API keys in production environments.

## Usage

1. Run the Streamlit application:

```bash
streamlit run image_caption_app.py
```

2. Access the application in your web browser (typically at http://localhost:8501)

3. Upload an image using the file uploader

4. Select your preferred description style from the dropdown menu

5. Click "Generate Description" to get your AI-generated caption

## How It Works

1. The application accepts image uploads from the user
2. The uploaded image is saved to a temporary file
3. The image is sent to Google's Gemini model along with a prompt based on the selected description style
4. Gemini analyzes the image and generates a description
5. The description is displayed on the web interface

## Dependencies

- [Streamlit](https://streamlit.io/) - Web application framework
- [Google Generative AI](https://aistudio.google.com/apikey) - AI model for image analysis and caption generation

## Security Note

The current code includes an API key directly in the source. For production use:

1. Move the API key to an environment variable or a secure configuration file
2. Add any configuration files with sensitive information to .gitignore

## Contribute

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Made with ❤️ by [Moosa Raza](https://www.linkedin.com/in/syed-moosa-raza-rizvi)

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Google for providing the Gemini AI model
- Streamlit for the excellent web app framework
