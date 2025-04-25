# utils.py
import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; font-size: 0.9em; color: gray;'>
            Built by <strong>Pranav Belligundu</strong> ·
            <a href='https://github.com/pranav-B21' target='_blank'>GitHub</a> ·
            <a href='https://linkedin.com/in/pranav-belligundu/' target='_blank'>LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )
