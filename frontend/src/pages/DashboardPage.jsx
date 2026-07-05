import { useEffect, useState } from "react";
import { apiRequest } from "../api/client";

export default function DashboardPage() {
  const [data, setData] = useState({ tests_completed: 0, avg_score: 0, accuracy_percent: 0 });

  const normalizedAccuracy = Math.max(0, Math.min(100, Number(data.accuracy_percent) || 0));
  const performanceTag =
    normalizedAccuracy >= 80 ? "Exam Ready" : normalizedAccuracy >= 60 ? "On Track" : "Needs Focus";
  const performanceHint =
    normalizedAccuracy >= 80
      ? "Great momentum. Maintain consistency and revise weak themes weekly."
      : normalizedAccuracy >= 60
        ? "Solid progress. Increase answer writing frequency for faster gains."
        : "Build daily discipline with short tests and targeted revision blocks.";

  useEffect(() => {
    apiRequest("/dashboard")
      .then(setData)
      .catch(() => setData({ tests_completed: 0, avg_score: 0, accuracy_percent: 0 }));
  }, []);

  return (
    <div className="dashboard-shell grid gap-16">
      <section className="card dashboard-hero">
        <div>
          <p className="dashboard-kicker">Lakshya Progress Console</p>
          <h2>Performance Dashboard</h2>
          <p className="muted">Track your UPSC preparation quality with a quick visual snapshot.</p>
        </div>
        <div className="dashboard-chip">{performanceTag}</div>
      </section>

      <section className="grid three-col dashboard-metrics">
        <div className="card metric-card metric-card-tests">
          <p className="metric-label">Tests Completed</p>
          <p>{data.tests_completed}</p>
          <span className="metric-foot">Consistency score driver</span>
        </div>
        <div className="card metric-card metric-card-score">
          <p className="metric-label">Average Score</p>
          <p>{data.avg_score}</p>
          <span className="metric-foot">Across submitted tests</span>
        </div>
        <div className="card metric-card metric-card-accuracy">
          <p className="metric-label">Accuracy</p>
          <p>{normalizedAccuracy}%</p>
          <span className="metric-foot">Current answer precision</span>
        </div>
      </section>

      <section className="grid two-col dashboard-insights">
        <div className="card progress-card">
          <h3>Accuracy Gauge</h3>
          <div
            className="accuracy-ring"
            style={{ background: `conic-gradient(#117f98 ${normalizedAccuracy}%, #dbe8ef ${normalizedAccuracy}% 100%)` }}
            aria-label={`Accuracy ${normalizedAccuracy} percent`}
          >
            <div className="accuracy-ring-inner">{normalizedAccuracy}%</div>
          </div>
          <div className="progress-track">
            <span style={{ width: `${normalizedAccuracy}%` }} />
          </div>
        </div>

        <div className="card insight-card">
          <h3>Coach Insight</h3>
          <p>{performanceHint}</p>
          <ul>
            <li>Set one daily prelims drill and one mains answer target.</li>
            <li>Review mistakes weekly and map them by GS topic.</li>
            <li>Use UPSC GPT for fast revision and concept checks.</li>
          </ul>
        </div>
      </section>

      <section className="card dashboard-footer-note">
        <strong>Tip:</strong> Keep improving $1\%$ daily. Compounded growth over 100 days gives a large edge.
      </section>
    </div>
  );
}
