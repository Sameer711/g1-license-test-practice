import streamlit as st
from urllib.parse import urlparse, parse_qs

# The list of questions and their correct answers
questions_data = [
    (1, 'c'), (2, 'b'), (3, 'b'), (4, 'd'), (5, 'a'), (6, 'd'), (7, 'c'), (8, 'b'), (9, 'b'), (10, 'a'),
    (11, 'a'), (12, 'c'), (13, 'd'), (14, 'a'), (15, 'c'), (16, 'b'), (17, 'c'), (18, 'd'), (19, 'c'), (20, 'b'),
    # Add remaining questions up to 201
]

# Inject custom CSS for larger radio buttons
st.markdown(
    """
    <style>
    .stRadio > div { 
        font-size: 20px; 
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
        st.write("Correct!")
        st.session_state.score += 1  # Increase score for correct answer
        st.session_state.show_next_button = True
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts < 2:
            st.write("Wrong! Try again.")
        else:
            st.write(f"Wrong! The correct answer is: {correct_answer}")
            st.session_state.show_next_button = True

# Function to move to the next question
def go_to_next_question():
    st.session_state.current_question_index += 1
    st.session_state.attempts = 0
    st.session_state.show_next_button = False
    # Update the URL to include the new question number as a permalink
    st.experimental_set_query_params(question=st.session_state.current_question_index + 1)

# Display the score
st.write(f"Score: {st.session_state.score}/{st.session_state.current_question_index}")

# Get the current question
current_question = questions_data[st.session_state.current_question_index]
question_text = f"Question {current_question[0]}"

# Display the question as a header
st.markdown(f"## {question_text}")

# Display the answer options with larger radio buttons
user_answer = st.radio('Choose your answer:', ['a', 'b', 'c', 'd'])

# Submit button for user to submit their answer
if st.button('Submit'):
    handle_answer(user_answer)

# Display the "Next Question" button if the user answered correctly or exhausted attempts
if st.session_state.show_next_button:
    if st.button('Next Question'):
        go_to_next_question()

# Display a message when the quiz is completed
if st.session_state.current_question_index >= len(questions_data):
    st.write("You've completed all the questions!")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions_data)}")
