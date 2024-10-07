import streamlit as st
from urllib.parse import urlparse, parse_qs

# Set the initial page configuration with a generic title
st.set_page_config(page_title="G1 License Test Practice", layout="centered")

# The list of questions and their correct answers
questions_data = [
    (1, 'c'), (2, 'b'), (3, 'b'), (4, 'd'), (5, 'a'), (6, 'd'), (7, 'c'), (8, 'b'), (9, 'b'), (10, 'a'),
    (11, 'a'), (12, 'c'), (13, 'd'), (14, 'a'), (15, 'c'), (16, 'b'), (17, 'c'), (18, 'd'), (19, 'c'), (20, 'b'),
    # Add remaining questions up to 201
]

# Inject custom CSS for larger feedback text and button styles
st.markdown(
    """
    <style>
    .feedback {
        font-size: 24px;
        font-weight: bold;
    }
    .stButton > button {
        width: 100%;
        padding: 15px;
        font-size: 20px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Initialize session state for tracking current question, attempts, score, and whether to show "Next Question" button
if 'current_question_index' not in st.session_state:
    st.session_state.curre
