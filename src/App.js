import React, { useState, useEffect } from 'react';
import { questionsData } from './questionsData';
import Question from './Question';
import Scoreboard from './Scoreboard';
import './App.css';

const App = () => {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [showNextButton, setShowNextButton] = useState(false);
  const [attempts, setAttempts] = useState(0);
  const [feedback, setFeedback] = useState(''); // New state to store feedback
  const [feedbackType, setFeedbackType] = useState(''); // New state for feedback type (correct or wrong)
  const [buttonsDisabled, setButtonsDisabled] = useState(false); // New state to disable buttons

  const currentQuestion = questionsData[currentQuestionIndex];

  // Function to handle the answer submission
  const handleAnswer = (answer) => {
    if (answer === currentQuestion.correctAnswer) {
      setScore(score + 1);
      setFeedback('Correct!');
      setFeedbackType('correct'); // Set feedback type as correct
      setShowNextButton(true);
      setButtonsDisabled(true); // Disable buttons after correct answer
    } else {
      setAttempts(attempts + 1);
      if (attempts >= 1) {
        setFeedback(`Wrong! The correct answer is: ${currentQuestion.correctAnswer.toUpperCase()}`);
        setFeedbackType('wrong'); // Set feedback type as wrong
        setShowNextButton(true); // Show "Next Question" button after 2 wrong attempts
        setButtonsDisabled(true); // Disable buttons after 2 wrong attempts
      } else {
        setFeedback('Wrong! Try again.');
        setFeedbackType('wrong'); // Set feedback type as wrong
      }
    }
  };

  // Function to go to the next question
  const goToNextQuestion = () => {
    setCurrentQuestionIndex(currentQuestionIndex + 1);
    setShowNextButton(false);
    setAttempts(0);
    setFeedback(''); // Reset feedback for the next question
    setFeedbackType(''); // Reset feedback type
    setButtonsDisabled(false); // Enable buttons for the next question
  };

  // Function to jump to a specific question
  const jumpToQuestion = (index) => {
    setCurrentQuestionIndex(index);
    setShowNextButton(false);
    setAttempts(0);
    setFeedback(''); // Reset feedback for the next question
    setFeedbackType(''); // Reset feedback type
    setButtonsDisabled(false); // Enable buttons for the next question
  };

  // Handle URL parameters for jumping to a specific question
  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const questionParam = urlParams.get('question');
    if (questionParam && !isNaN(questionParam)) {
      const questionIndex = parseInt(questionParam) - 1;
      if (questionIndex >= 0 && questionIndex < questionsData.length) {
        setCurrentQuestionIndex(questionIndex);
      }
    }
  }, []);

  return (
    <div className="App">
      <h1>G1 License Test Practice</h1>

      {/* Permalinks to jump to specific questions */}
      <div className="permalinks">
        <button onClick={() => jumpToQuestion(50)}>Go to Question 51</button>
        <button onClick={() => jumpToQuestion(100)}>Go to Question 101</button>
        <button onClick={() => jumpToQuestion(150)}>Go to Question 151</button>
      </div>

      <Scoreboard score={score} questionNumber={currentQuestionIndex + 1} />
      <Question
        questionId={currentQuestion.id}
        handleAnswer={handleAnswer}
        disabled={buttonsDisabled} // Pass the disabled state to the Question component
      />
      
      {/* Display feedback with dynamic class based on feedback type */}
      {feedback && (
        <p className={`feedback ${feedbackType === 'correct' ? 'feedback-correct' : 'feedback-wrong'}`}>
          {feedback}
        </p>
      )}

      {showNextButton && (
        <button onClick={goToNextQuestion}>Next Question</button>
      )}
    </div>
  );
};

export default App;
