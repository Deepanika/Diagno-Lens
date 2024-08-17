# importing the necessary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import api_key
import io
import tempfile

# configure with genai api key
genai.configure(api_key=api_key)
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)


system_prompt = """

As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are "Unable to be determined based on the provided image."
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."
4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structural approach mentioned above.

"""

# Streamlit page setup
st.set_page_config(page_title="Your Virtual Medical Assistor", page_icon=":robot:")
st.title("Your Virtual Medical Assistor")
st.subheader("A virtual assistor that helps to analyse the medical images")

# File uploader for medical images
uploaded_file = st.file_uploader("Upload the image for analysis",type=["png","jpg","jpeg"])


if uploaded_file:
    st.image(uploaded_file,width=300,caption="Uploaded Iamge for analysis")
    submit_button = st.button("Generate the analysis!")

    if submit_button:
        # Try to process the uploaded image
        try:
            image_data = uploaded_file.getvalue()

            # Create a temporary file to store the image data
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                temp_file.write(image_data)
                temp_file_path = temp_file.name

            # Upload the image using the temporary file path
            file = genai.upload_file(temp_file_path, mime_type="image/jpeg")
            files = [file]

            # Create a chat session with the system prompt and user input
            chat_session = model.start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": [files[0], system_prompt],
                    },
                    {
                        "role": "model",
                        "parts": ["I am sharing the analysis"],
                    },
                ]
            )
            
            
            # Send the message for analysis
            response = chat_session.send_message("Analyzing the provided medical image.")
            if response:
                st.title("Analysis Result")
                st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            
        Path(temp_file_path).unlink()

else:
    st.warning("Please upload an image first.")