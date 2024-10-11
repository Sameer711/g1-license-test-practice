import React from 'react';

const Question = ({ questionId, handleAnswer, disabled }) => {
  return (
    <div className="question">
      <h2>Question {questionId}</h2>
      <div>
        <button onClick={() => handleAnswer('a')} disabled={disabled}>A</button>
        <button onClick={() => handleAnswer('b')} disabled={disabled}>B</button>
        <button onClick={() => handleAnswer('c')} disabled={disabled}>C</button>
        <button onClick={() => handleAnswer('d')} disabled={disabled}>D</button>
      </div>
    </div>
  );
};

export default Question;
