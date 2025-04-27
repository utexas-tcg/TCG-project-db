import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Set config and hide sidebar
st.set_page_config(page_title="TCG Dashboard", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "Search", "Upload"],
    icons=["house", "search", "cloud-upload"],
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
