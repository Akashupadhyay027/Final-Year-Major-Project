import streamlit as st

def show():
    # Make sure we use a cool, techy layout
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.title("Sign Language Detection & Translation V1.0")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Welcome to the Future of Communication!
    This system bridges the gap between sign language and spoken/written words using cutting-edge Deep Learning & Computer Vision.
    
    👈 **Use the sidebar to navigate to the Detection Engine.**
    """)
    
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.subheader("How It Works")
    st.write("1. Head over to the **Detection** tab.")
    st.write("2. Ensure your webcam is enabled and you are well-lit.")
    st.write("3. Perform sign language gestures.")
    st.write("4. Watch as our AI translates your signs into text in real-time!")
    st.markdown('</div>', unsafe_allow_html=True)

    # Adding a nice image or placeholder visualization
    st.image("https://www.verywellhealth.com/thmb/Bw86lHlF2bM-7O2pM_k2b7O8nQ0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1216654227-2e86b4a5351e44f595b1116c4f03c0db.jpg", caption="Bridging the Communication Gap", use_column_width=True)
