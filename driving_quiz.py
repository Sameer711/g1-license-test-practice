import streamlit as st
from questions_data import questions_data  # Import questions_data from the new file

# Set the initial page configuration
st.set_page_config(page_title="G1 License Test Practice", layout="centered")

# Inject custom CSS for styling
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

# Initialize session state for current question index, attempts, score, and show_next_button
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

if 'show_next_button' not in st.session_state:
    st.session_state.show_next_button = False

if 'score' not in st.session_state:
    st.session_state.score = 0

# Function to move to the next question
def go_to_next_question():
    st.session_state.current_question_index += 1
    st.session_state.attempts = 0
    st.session_state.show_next_button = False
    # Update the URL to include the new question number as a query parameter
    st.experimental_set_query_params(question=st.session_state.current_question_index + 1)
    question_text = f"Question {st.session_state.current_question_index}"

# Get query parameters and update the question number if necessary
query_params = st.experimental_get_query_params()
if 'question' in query_params:
    try:
        question_index = int(query_params['question'][0]) - 1
        if 0 <= question_index < len(questions_data):
            st.session_state.current_question_index = question_index
    except (ValueError, IndexError):
        pass

# Get the current question
current_question = questions_data[st.session_state.current_question_index]
question_text = f"Question {current_question[0]}"

# Inject JavaScript to update the title immediately after question changes
st.markdown(
    f"""
    <script>
    document.title = 'G1 License Test Practice Question {current_question[0]}';
    </script>
    """,
    unsafe_allow_html=True
)

# Function to handle answer submission
def handle_answer(user_answer):
    current_question = questions_data[st.session_state.current_question_index]
    correct_answer = current_question[1]

    if user_answer == correct_answer:
        st.markdown("<div class='feedback'>Correct!</div>", unsafe_allow_html=True)
        st.session_state.score += 1
        st.session_state.show_next_button = True
        # Play correct sound
        st.markdown("<script>var audio = new Audio('https://www.soundjay.com/button/beep-07.wav'); audio.play();</script>", unsafe_allow_html=True)
    else:
        st.session_state.attempts += 1
        if st.session_state.attempts < 2:
            st.write("Wrong! Try again.")
        else:
            st.markdown(f"<div class='feedback'>Wrong! The correct answer is: {correct_answer.upper()}</div>", unsafe_allow_html=True)
            st.session_state.show_next_button = True

# Display the score and update it based on the number of questions answered
score_text = f"Score: {st.session_state.score}/{st.session_state.current_question_index + 1}"
st.write(score_text)

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
