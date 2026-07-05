import { Link } from "react-router-dom";

const cards = [
  { title: "UPSC GPT", to: "/upsc-gpt", desc: "Ask UPSC questions and evaluate uploaded PDFs." },
  { title: "Test Generator", to: "/test-generator", desc: "Generate Prelims and Mains tests with AI." },
  { title: "Mains Evaluator", to: "/mains-evaluator", desc: "Upload answers for examiner-style evaluation." },
  { title: "Current Affairs", to: "/current-affairs", desc: "Browse topic-tagged UPSC current affairs." },
  { title: "UPSC Puzzle", to: "/upsc-puzzle", desc: "Gamified PYQ puzzle mode for active practice." },
  { title: "Dashboard", to: "/dashboard", desc: "Track your progress and test performance." },
];

export default function HomePage() {
  return (
    <div>
      <h2>Welcome to Lakshya</h2>
      <p className="muted">Master UPSC with AI-powered modules.</p>
      <div className="grid two-col">
        {cards.map((card) => (
          <Link key={card.to} className="card feature-card" to={card.to}>
            <h3>{card.title}</h3>
            <p>{card.desc}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
