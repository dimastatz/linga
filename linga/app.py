""" test pdf reader """

import base64
from PIL import Image
import streamlit as st
from streamlit.logger import get_logger
from streamlit_drawable_canvas import st_canvas


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

drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == "point":
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

Canvas = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == "point" else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
if Canvas.image_data is not None:
    st.image(Canvas.image_data)
