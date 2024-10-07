import streamlit as st
from urllib.parse import urlencode, urlparse, parse_qs

# The list of questions and their correct answers
questions_data = [
    (1, 'c'), (2, 'b'), (3, 'b'), (4, 'd'), (5, 'a'), (6, 'd'), (7, 'c'), (8, 'b'), (9, 'b'), (10, 'a'),
    (11, 'a'), (12, 'c'), (13, 'd'), (14, 'a'), (15, 'c'), (16, 'b'), (17, 'c'), (18, 'd'), (19, 'c'), (20, 'b'),
    (21, 'c'), (22, 'a'), (23, 'a'), (24, 'b'), (25, 'a'), (26, 'a'), (27, 'b'), (28, 'd'), (29, 'd'), (30, 'b'),
    # Add remaining questions up to 201
]

# Get query parameters
parsed_url = urlparse(st.experimental_get_query_params())
query_params = parse_qs(parsed_url.query)

# Get question number from the URL, default to 1 if not present
current_question_number = int(query_params.get('q', [1])[0])

# Create a slider to navigate through questions
question_number = st.slider('Question Number', 1, len(questions_data), value=current_question_number)

# Create permalink for the current question
st.markdown(f"[Permalink to this question](?{urlencode({'q': question_number})})")

# Get the current question and its answer
current_question = questions_data[question_number - 1]
question_text = f"Question {current_question[0]}"
correct_answer = current_question[1]

# Initialize session state variables
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'answered_correctly' not in st.session_state:
    st.session_state.answered_correctly = False

# Display the question and options
st.write(question_text)
user_answer = st.radio('Choose your answer:', ['a', 'b', 'c', 'd'])

# Submit button logic
if st.button('Submit'):
    # Check if user has already answered correctly
    if not st.session_state.answered_correctly:
        if user_answer == correct_answer:
            st.write("Correct!")
            st.session_state.answered_correctly

