import streamlit as st
from streamlit_option_menu import option_menu
import importlib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from .env file
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# Set config and hide sidebar
st.set_page_config(page_title="TCG Dashboard", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login function
def authenticate(username, password):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        st.session_state.authenticated = True
        return True
    return False

# Login screen
if not st.session_state.authenticated:
    # Center the login form with custom CSS
    st.markdown("""
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 30vh;
            text-align: center;
            margin-bottom: -50px;
        }
        </style>
        <div class="login-container">
            <h1>Log In</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Create columns to center the form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
        
        if login_button:
            if authenticate(username, password):
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

# Only show the main app if authenticated
else:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Edit", "Upload", "Add_Project"],
        icons=["house", "pencil-square", "cloud-upload", "plus-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#0E1117",
                "display": "flex",
                "justify-content": "center"
            },
            "icon": {
                "color": "white",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "18px", 
                "text-align": "center",
                "margin": "0 12px",
                "color": "white",
                "--hover-color": "rgba(10, 10, 69, 0.3)",  # transparent hover
                "border": "1px solid black",
                "border-radius": "10px" 
            },
            "nav-link-selected": {
                "background-color": "#0A0A45",
                "color": "white",
                "border": "2px solid black",
                "border-radius": "10px"
            }
        }
    )

    # Load corresponding module
    module_name = f"pages.{selected}"
    module = importlib.import_module(module_name)
    if hasattr(module, "main"):
        module.main()
