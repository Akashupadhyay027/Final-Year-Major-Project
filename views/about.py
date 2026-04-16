import streamlit as st

def show():
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.title("About This Project")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    ### Final Year Major Project
    This application represents a comprehensive effort to build a robust, real-time gesture recognition system.
    """)
    
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.subheader("Technology Stack")
    st.markdown("""
    - **Frontend:** Streamlit 🎈
    - **Computer Vision:** OpenCV
    - **Machine Learning / Deep Learning:** [Placeholder: MediaPipe / TensorFlow / YOLO]
    - **Language:** Python
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.subheader("The Team")
    st.write("Designed and developed with ❤️ for the Final Year Project.")
    st.markdown('</div>', unsafe_allow_html=True)
