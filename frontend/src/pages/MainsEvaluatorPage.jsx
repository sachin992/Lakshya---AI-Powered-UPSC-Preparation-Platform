import { useState } from "react";
import { apiRequest } from "../api/client";

export default function MainsEvaluatorPage() {
  const [threadId] = useState(() => crypto.randomUUID());
  const [paper, setPaper] = useState("GS Paper I");
  const [marks, setMarks] = useState(10);
  const [mode, setMode] = useState("Hard");
  const [question, setQuestion] = useState("");
  const [status, setStatus] = useState("");
  const [evaluation, setEvaluation] = useState("");

  const upload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      const data = await apiRequest(`/mains/upload?thread_id=${encodeURIComponent(threadId)}`, {
        method: "POST",
        body: formData,
      });
      setStatus(`Indexed ${data.metadata.filename}`);
    } catch (err) {
      setStatus(`Upload failed: ${err.message}`);
    }
  };

  const evaluate = async () => {
    setEvaluation("Evaluating...");
    try {
      const data = await apiRequest("/mains/evaluate", {
        method: "POST",
        body: JSON.stringify({ thread_id: threadId, paper, marks, mode, question }),
      });
      setEvaluation(data.evaluation);
    } catch (err) {
      setEvaluation(`Evaluation failed: ${err.message}`);
    }
  };

  return (
    <div className="card grid gap-16">
      <h2>Mains Evaluator</h2>
      <p className="muted">Thread ID: {threadId}</p>
      <div className="grid two-col">
        <select value={paper} onChange={(e) => setPaper(e.target.value)}>
          <option>GS Paper I</option>
          <option>GS Paper II</option>
          <option>GS Paper III</option>
          <option>GS Paper IV</option>
          <option>Essay</option>
          <option>Optional</option>
        </select>
        <select value={marks} onChange={(e) => setMarks(Number(e.target.value))}>
          <option value={10}>10</option>
          <option value={15}>15</option>
          <option value={20}>20</option>
        </select>
        <select value={mode} onChange={(e) => setMode(e.target.value)}>
          <option>Hard</option>
          <option>Easy</option>
        </select>
        <input type="file" accept="application/pdf" onChange={upload} />
      </div>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Question (optional)" />
      {status && <p className="muted">{status}</p>}
      <button className="primary-btn" onClick={evaluate}>
        Evaluate Answer
      </button>
      {evaluation && <pre className="result-pre">{evaluation}</pre>}
    </div>
  );
}
