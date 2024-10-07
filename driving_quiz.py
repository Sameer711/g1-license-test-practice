import streamlit as st

# The list of questions and their correct answers
questions_data = [
    (1, 'c'), (2, 'b'), (3, 'b'), (4, 'd'), (5, 'a'), (6, 'd'), (7, 'c'), (8, 'b'), (9, 'b'), (10, 'a'),
    (11, 'a'), (12, 'c'), (13, 'd'), (14, 'a'), (15, 'c'), (16, 'b'), (17, 'c'), (18, 'd'), (19, 'c'), (20, 'b'),
    (21, 'c'), (22, 'a'), (23, 'a'), (24, 'b'), (25, 'a'), (26, 'a'), (27, 'b'), (28, 'd'), (29, 'd'), (30, 'b'),
    (31, 'd'), (32, 'c'), (33, 'b'), (34, 'a'), (35, 'c'), (36, 'b'), (37, 'd'), (38, 'b'), (39, 'c'), (40, 'c'),
    (41, 'b'), (42, 'd'), (43, 'b'), (44, 'c'), (45, 'c'), (46, 'c'), (47, 'a'), (48, 'b'), (49, 'd'), (50, 'd'),
    (51, 'c'), (52, 'a'), (53, 'a'), (54, 'd'), (55, 'b'), (56, 'd'), (57, 'd'), (58, 'b'), (59, 'b'), (60, 'a'),
    (61, 'a'), (62, 'c'), (63, 'a'), (64, 'b'), (65, 'd'), (66, 'a'), (67, 'c'), (68, 'a'), (69, 'b'), (70, 'd'),
    (71, 'd'), (72, 'd'), (73, 'b'), (74, 'a'), (75, 'd'), (76, 'd'), (77, 'b'), (78, 'b'), (79, 'a'), (80, 'd'),
    (81, 'a'), (82, 'a'), (83, 'c'), (84, 'a'), (85, 'd'), (86, 'b'), (87, 'c'), (88, 'd'), (89, 'a'), (90, 'c'),
    (91, 'b'), (92, 'b'), (93, 'a'), (94, 'd'), (95, 'c'), (96, 'd'), (97, 'b'), (98, 'b'), (99, 'a'), (100, 'd'),
    (101, 'a'), (102, 'a'), (103, 'c'), (104, 'a'), (105, 'd'), (106, 'b'), (107, 'c'), (108, 'd'), (109, 'a'), (110, 'c'),
    (111, 'b'), (112, 'b'), (113, 'a'), (114, 'd'), (115, 'a'), (116, 'c'), (117, 'a'), (118, 'b'), (119, 'c'), (120, 'b'),
    (121, 'b'), (122, 'a'), (123, 'a'), (124, 'a'), (125, 'c'), (126, 'b'), (127, 'd'), (128, 'c'), (129, 'd'), (130, 'd'),
    (131, 'c'), (132, 'a'), (133, 'd'), (134, 'c'), (135, 'c'), (136, 'c'), (137, 'a'), (138, 'c'), (139, 'b'), (140, 'b'),
    (141, 'b'), (142, 'd'), (143, 'd'), (144, 'a'), (145, 'b'), (146, 'b'), (147, 'a'), (148, 'd'), (149, 'c'), (150, 'a'),
    (151, 'b'), (152, 'd'), (153, 'b'), (154, 'c'), (155, 'd'), (156, 'a')
]

# Create a slider to navigate through questions
question_number = st.slider('Question Number', 1, len(questions_data))

# Get the current question and its answer
current_question = questions_data[question_number - 1]
question_text = f"Question {current_question[0]}"
correct_answer = current_question[1]

# Display the question and options
st.write(question_text)
user_answer = st.radio('Choose your answer:', ['a', 'b', 'c', 'd'])

# Check if the user answered correctly
if st.button('Submit'):
    if user_answer == correct_answer:
        st.write("Correct!")
    else:
        st.write(f"Wrong! The correct answer is: {correct_answer}")

