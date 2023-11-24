""" test pdf reader """

import base64
import streamlit as st
from streamlit.logger import get_logger


logger = get_logger(__name__)

st.set_page_config(page_title="pdf-GPT", page_icon="📖", layout="wide")
st.header("pdf-GPT")
logger.info("header set")


def clear_submit():
    """submit = false"""
    st.session_state["submit"] = False


def show_pdf(file_path):
    """load pdf content"""
    with open(file_path, "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode("utf-8")
        logger.info("pdf is loaded {len(base64_pdf)}")

    pdf_display = (
        f'<iframe src="data:application/pdf;base64,{base64_pdf}"'
        + 'width="800" height="800" type="application/pdf"></iframe>'
    )
    st.markdown(pdf_display, unsafe_allow_html=True)


show_pdf("./docs/comics.pdf")
