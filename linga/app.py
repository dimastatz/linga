""" test pdf reader """

import streamlit as st


st.set_page_config(page_title="pdf-GPT", page_icon="📖", layout="wide")
st.header("pdf-GPT")


def clear_submit():
    """ submit = false """
    st.session_state["submit"] = False
