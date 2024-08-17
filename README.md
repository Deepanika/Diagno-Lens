# Diagno-Lens
This project is a Streamlit-based web application designed to assist medical professionals in analyzing medical images. Leveraging the power of Google Generative AI's Gemini 1.5 Flash model, this virtual assistor provides a detailed examination of medical images, identifies anomalies or potential health issues, and offers recommendations on next steps, including further tests or treatments.

Features:
File Upload: Easily upload medical images (PNG, JPG, JPEG) for analysis.
AI-Powered Analysis: Utilizes Google's advanced Gemini 1.5 Flash model to analyze medical images for any potential anomalies, diseases, or health issues.
Recommendations & Treatment: Provides next steps, potential further tests, and treatment options if applicable.
Image Quality Disclaimer: Automatically notes any cases where image quality is insufficient for a thorough analysis.
Doctor Consultation: Accompanies all responses with a disclaimer urging consultation with a medical professional before taking any action.
Technologies Used:
Streamlit: For building the web interface.
Google Generative AI: For performing the image analysis.
Python: Primary language for the backend processing and integration.
How to Run Locally:
Clone the repository.
Install the necessary dependencies using pip install -r requirements.txt.
Set up your Google Generative AI API key.
Run the Streamlit app using streamlit run app.py.
Upload a medical image and generate a detailed AI analysis.
Disclaimer:
This tool is intended to assist with image analysis but is not a substitute for professional medical diagnosis. Always consult with a healthcare provider before making any medical decisions.
 
