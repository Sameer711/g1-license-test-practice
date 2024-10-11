import React from 'react';

const Scoreboard = ({ score, questionNumber }) => {
  return (
    <div className="scoreboard">
      <p>Score: {score}</p>
    </div>
  );
};

export default Scoreboard;
