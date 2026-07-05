import { useMemo, useState } from "react";
import { apiRequest } from "../api/client";

export default function TestGeneratorPage() {
  const [form, setForm] = useState({
    exam_type: "Prelims",
    paper_type: "General Studies (Paper I)",
    num_questions: 5,
    question_source: "Mock Questions",
    ca_integration: "Off",
    preferences: "",
    language: "English",
  });
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);

  const update = (e) => {
    const { name, value } = e.target;
    setForm((p) => ({ ...p, [name]: name === "num_questions" ? Number(value) : value }));
  };

  const generate = async () => {
    const data = await apiRequest("/tests/generate", {
      method: "POST",
      body: JSON.stringify(form),
    });
    setQuestions(data.questions || []);
    setAnswers({});
    setResult(null);
  };

  const submit = async () => {
    if (!questions.length) return;
    let score = 0;
    let maxScore = 0;

    if (form.exam_type === "Prelims") {
      questions.forEach((q) => {
        const marks = q.marks || 2;
        maxScore += marks;
        if (answers[q.id] === q.correct_answer) score += marks;
      });
    } else {
      maxScore = questions.reduce((sum, q) => sum + (q.marks || 10), 0);
      score = Object.keys(answers).length;
    }

    const payload = {
      exam_type: form.exam_type,
      paper_type: form.paper_type,
      total_questions: questions.length,
      score,
      max_score: maxScore,
      result_json: JSON.stringify({ answers, questions }),
    };

    await apiRequest("/tests/submit", {
      method: "POST",
      body: JSON.stringify(payload),
    });

    setResult({ score, maxScore });
  };

  const isPrelims = useMemo(() => form.exam_type === "Prelims", [form.exam_type]);

  return (
    <div className="grid gap-16">
      <div className="card">
        <h2>Test Generator</h2>
        <div className="grid two-col">
          <select name="exam_type" value={form.exam_type} onChange={update}>
            <option>Prelims</option>
            <option>Mains</option>
          </select>
          <input name="paper_type" value={form.paper_type} onChange={update} placeholder="Paper type" />
          <input
            type="number"
            name="num_questions"
            value={form.num_questions}
            min={1}
            max={50}
            onChange={update}
          />
          <select name="question_source" value={form.question_source} onChange={update}>
            <option>Mock Questions</option>
            <option>Previous Year Questions</option>
            <option>Mixed (Mocks & PYQs)</option>
          </select>
          <select name="ca_integration" value={form.ca_integration} onChange={update}>
            <option>Off</option>
            <option>On</option>
          </select>
          <select name="language" value={form.language} onChange={update}>
            <option>English</option>
            <option>Hindi</option>
          </select>
        </div>
        <textarea
          name="preferences"
          value={form.preferences}
          onChange={update}
          placeholder="Additional preferences"
        />
        <button className="primary-btn" onClick={generate}>
          Generate Test
        </button>
      </div>

      {!!questions.length && (
        <div className="card">
          <h3>Questions</h3>
          {questions.map((q) => (
            <div key={q.id} className="question-block">
              <p>
                <strong>Q{q.id}.</strong> {q.question}
              </p>
              {isPrelims ? (
                <div className="grid two-col">
                  {Object.entries(q.options || {}).map(([key, val]) => (
                    <label key={key} className="option-row">
                      <input
                        type="radio"
                        name={`q-${q.id}`}
                        value={key}
                        checked={answers[q.id] === key}
                        onChange={() => setAnswers((a) => ({ ...a, [q.id]: key }))}
                      />
                      {key}) {val}
                    </label>
                  ))}
                </div>
              ) : (
                <textarea
                  placeholder="Write your answer"
                  value={answers[q.id] || ""}
                  onChange={(e) => setAnswers((a) => ({ ...a, [q.id]: e.target.value }))}
                />
              )}
            </div>
          ))}
          <button className="primary-btn" onClick={submit}>
            Submit Test
          </button>
          {result && (
            <p className="success-text">
              Saved. Score: {result.score}/{result.maxScore}
            </p>
          )}
        </div>
      )}
    </div>
  );
}
