import streamlit as st
import cv2
import numpy as np

# Absolute imports - adjust if package structure changes
from utils.video_utils import annotate_frame
from utils.model_utils import predict_sign, load_system_model

def show():
    # Cache the model load so we don't reload it every frame loop
    @st.cache_resource
    def get_model():
        return load_system_model()
        
    model = get_model()

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.title("Real-Time Detection Engine")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### Live Feed")
        run = st.checkbox("Start Webcam", key="start_webcam")
        FRAME_WINDOW = st.image([])
        
    with col2:
        st.markdown("### Detected Sign")
        sign_display = st.empty()
        sign_display.markdown('<div class="translation-box">Standby</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.write("**Model Status:**")
        st.success(f"{model['status']}")
        
    camera = None
    if run:
        # 0 is usually the built-in webcam
        camera = cv2.VideoCapture(0)
        
        while run:
            ret, frame = camera.read()
            
            if not ret:
                st.error("Failed to access webcam.")
                break
                
            # Convert BGR (OpenCV) to RGB (Streamlit)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Predict the sign
            prediction = predict_sign(frame_rgb, model)
            
            # Annotate the frame with the prediction
            annotated_frame = annotate_frame(frame_rgb.copy(), prediction)
            
            # Update the UI
            FRAME_WINDOW.image(annotated_frame)
            
            # Update the text box. The div formatting gives it a "glow" UI.
            sign_display.markdown(f'<div class="translation-box">{prediction}</div>', unsafe_allow_html=True)
            
    elif camera is not None:
        camera.release()
