import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image
import cv2
import google.generativeai as genai

# Load the logo image
st.write("")
st.write("")
# logo = Image.open('daffodil-logo-black.png')

# # Display the logo and title in the header
# col1, col2 = st.columns([1, 8])
# with col1:
#     st.image(logo, use_column_width=True)
# with col2:
#     st.title("Smart Food Analyzer: Detect & Analyze Your Meal")

# # Information about the classes
# st.write("**Number of classes:** 7")
# st.write("1. Roti")
# st.write("2. Rice")
# st.write("3. Rajma")
# st.write("4. Dal Fry")
# st.write("5. Dal Makhani")
# st.write("6. Kadhi")
# st.write("7. Mix Veg")

# option = st.radio("Choose how to provide the image:", ('Upload Image', 'Select Image from List'))

# uploaded_file = None

# if option == 'Upload Image':
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# else:
#     image_paths = [f"img_{i}.jpg" for i in range(1, 21)]
#     uploaded_file = st.selectbox("Choose an image for inference...", image_paths)

# if uploaded_file is not None:
#     if option == 'Upload Image':
#         image = Image.open(uploaded_file)
#     else:
#         image = Image.open(uploaded_file)
    
#     st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

#     st.write("### Custom Model Output:")
    
#     # Run YOLO inference
#     model = YOLO('model-5.pt')  
#     results = model.predict(source=image, device='cpu')

#     # Convert PIL image to displayable format for bounding boxes
#     image = np.array(image)

#     # Draw bounding boxes
#     for result in results:
#         for detection in result.boxes:
#             x1, y1, x2, y2 = map(int, detection.xyxy[0])
#             confidence = float(detection.conf[0])
#             class_id = int(detection.cls[0])
#             label = f"{model.names[class_id]}: {confidence:.2f}"
#             color = (0, 255, 0)

#             # Draw the bounding box and label on the image
#             cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
#             cv2.putText(image, label, (x1+5, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

#     # Display the result image
#     st.image(image, caption='Processed Image.', use_column_width=True)

#     genai.configure(api_key="AIzaSyDQWSzO_GhPrvfBIN6_LDLehTB_6MXeie8")
#     model = genai.GenerativeModel('gemini-1.5-pro')

#     # Assuming the Gemini API expects an image file
#     sample_file = Image.open(uploaded_file)

#     response = model.generate_content([sample_file, "Identify the food in the image.\
#                                                    Give rough portion size and nutritional values in a table format.\
#                                                    Do not include any other text or explanations."])
    
#     st.write("### LLM Output:")
#     st.write(response.text)
