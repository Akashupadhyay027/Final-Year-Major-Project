import streamlit as st
import os

# Set page config FIRST
st.set_page_config(
    page_title="Sign Language AI",
    page_icon="🖐️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    """Loads the custom CSS for styling the dashboard"""
    css_file = os.path.join("assets", "style.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load styles
load_css()

# Import the view modules
from views import home, detection, about

def main():
    st.sidebar.markdown("## 🧭 Navigation")
    
    # Beautiful sidebar buttons/radio
    menu = ["🏠 Home", "🎥 Detection Engine", "ℹ️ About"]
    choice = st.sidebar.radio("Go to", menu)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### System Status")
    st.sidebar.success("Backend Online")
    st.sidebar.info("Camera Ready")

    # Routing
    if choice == "🏠 Home":
        home.show()
    elif choice == "🎥 Detection Engine":
        detection.show()
    elif choice == "ℹ️ About":
        about.show()

if __name__ == '__main__':
    main()
