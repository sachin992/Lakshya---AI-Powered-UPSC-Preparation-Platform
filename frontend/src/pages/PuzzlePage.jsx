import { useMemo, useState } from "react";
import { apiRequest } from "../api/client";

export default function PuzzlePage() {
  const [seed] = useState(() => crypto.randomUUID());
  const [grid, setGrid] = useState([]);
  const [gridSize, setGridSize] = useState(5);
  const [totalQuestions, setTotalQuestions] = useState(6);
  const [revealed, setRevealed] = useState(new Set());
  const [score, setScore] = useState(0);
  const [question, setQuestion] = useState(null);
  const [selected, setSelected] = useState("");

  const questionPositions = useMemo(() => new Set(grid), [grid]);

  const init = async () => {
    const data = await apiRequest("/puzzle/init", {
      method: "POST",
      body: JSON.stringify({ seed, grid_size: gridSize, total_questions: totalQuestions }),
    });
    setGrid(data.question_positions || []);
    setRevealed(new Set());
    setScore(0);
    setQuestion(null);
  };

  const clickCell = async (idx) => {
    if (revealed.has(idx)) return;
    if (questionPositions.has(idx)) {
      const data = await apiRequest("/puzzle/question", {
        method: "POST",
        body: JSON.stringify({ category: "History & Culture" }),
      });
      setQuestion(data);
      setRevealed((prev) => new Set(prev).add(idx));
    } else {
      setRevealed((prev) => new Set(prev).add(idx));
    }
  };

  const submitAnswer = async () => {
    if (!question || !selected) return;
    const correct = question.correct;
    const payload = { selected: selected.split(")")[0], correct };
    const data = await apiRequest("/puzzle/score", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    setScore((s) => s + (data.score_delta || 0));
    setQuestion(null);
    setSelected("");
  };

  return (
    <div className="grid gap-16">
      <div className="card">
        <h2>UPSC Puzzle</h2>
        <div className="grid two-col">
          <select value={gridSize} onChange={(e) => setGridSize(Number(e.target.value))}>
            <option value={5}>Beginner (5x5)</option>
            <option value={6}>Intermediate (6x6)</option>
            <option value={8}>Advanced (8x8)</option>
          </select>
          <select value={totalQuestions} onChange={(e) => setTotalQuestions(Number(e.target.value))}>
            <option value={6}>6 questions</option>
            <option value={8}>8 questions</option>
            <option value={12}>12 questions</option>
          </select>
        </div>
        <button className="primary-btn" onClick={init}>
          Start Puzzle
        </button>
        <p className="muted">Score: {score}</p>
      </div>

      {!!grid.length && (
        <div className="card">
          <div className="puzzle-grid" style={{ gridTemplateColumns: `repeat(${gridSize}, 1fr)` }}>
            {Array.from({ length: gridSize * gridSize }).map((_, idx) => (
              <button key={idx} className="cell" onClick={() => clickCell(idx)}>
                {revealed.has(idx) ? (questionPositions.has(idx) ? "?" : "") : ""}
              </button>
            ))}
          </div>
        </div>
      )}

      {question && (
        <div className="card">
          <h3>{question.question}</h3>
          <p className="muted">{question.year}</p>
          {question.options.map((opt) => (
            <label key={opt} className="option-row">
              <input
                type="radio"
                name="puzzle-opt"
                value={opt}
                checked={selected === opt}
                onChange={(e) => setSelected(e.target.value)}
              />
              {opt}
            </label>
          ))}
          <button className="primary-btn" onClick={submitAnswer}>
            Submit Answer
          </button>
        </div>
      )}
    </div>
  );
}
