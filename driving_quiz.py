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
    st.session_state.current_question_index = 0  # Start with the first question

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

if 'show_next_button' not in st.session_state:
    st.session_state.show_next_button = False

if 'score' not in st.session_state:
    st.session_state.score = 0

# Display the navigation permalinks at the top
st.markdown(
    """
    [Go to Question 1](?question=1) | [Go to Question 51](?question=51) | [Go to Question 101](?question=101) | [Go to Question 151](?question=151)
    """
)

# Get query parameters and handle '/question/x' URLs
query_params = st.experimental_get_query_params()
if 'question' in query_params:
    try:
        question_index = int(query_params['question'][0]) - 1  # Convert to zero-based index
        if 0 <= question_index < len(questions_data):
            st.session_state.current_question_index = question_index
    except (ValueError, IndexError):
        pass

# Function to handle answer submission
def handle_answer(user_answer):
    current_question = questions_data[st.session_state.current_question_index]
    correct_answer = current_question[1]

    # Check if the answer is correct
    if user_answer == correct_answer:
        st.markdown("<div class='feedback'>Correct!</div>", unsafe_allow_html=True)
        st.session_state.score += 1  # Increase score for correct answer
        st.session_state.show_next_button = True
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts < 2:
            st.write("Wrong! Try again.")
        else:
            st.markdown(f"<div class='feedback'>Wrong! The correct answer is: {correct_answer.upper()}</div>", unsafe_allow_html=True)
            st.session_state.show_next_button = True

# Function to move to the next question
def go_to_next_question():
    st.session_state.current_question_index += 1
    st.session_state.attempts = 0
    st.session_state.show_next_button = False
    # Update the URL to include the new question number as a permalink
    st.experimental_set_query_params(question=st.session_state.current_question_index + 1)

# Get the current question
current_question = questions_data[st.session_state.current_question_index]
question_text = f"Question {current_question[0]}"

# Dynamically set the page title to include the current question number using JavaScript
st.markdown(
    f"""
    <script>
    document.title = 'G1 License Test Practice Question {current_question[0]}';
    </script>
    """, 
    unsafe_allow_html=True
)

# Display the score
st.write(f"Score: {st.session_state.score}/{st.session_state.current_question_index}")

# Display the question as a header
st.markdown(f"## {question_text}")

# Display the answer buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('A'):
        handle_answer('a')
with col2:
    if st.button('B'):
        handle_answer('b')
with col3:
    if st.button('C'):
        handle_answer('c')
with col4:
    if st.button('D'):
        handle_answer('d')

# Display the "Next Question" button if the user answered correctly or exhausted attempts
if st.session_state.show_next_button:
    if st.button('Next Question'):
        go_to_next_question()

# Display a message when the quiz is completed
if st.session_state.current_question_index >= len(questions_data):
    st.write("You've completed all the questions!")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions_data)}")
