import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login, register } = useAuth();
  const [isSignup, setIsSignup] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    phone: "",
    password: "",
    bpsc_attempt: "72nd",
    commitment_4hrs: false,
  });

  const onChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm((prev) => ({ ...prev, [name]: type === "checkbox" ? checked : value }));
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setIsSubmitting(true);
    try {
      if (isSignup) {
        await register(form);
      } else {
        await login(form.email, form.password);
      }
      navigate("/");
    } catch (err) {
      setError(err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-orbit" aria-hidden="true">
        <div className="orbit-ring" />
        <div className="orbit-core">LI</div>
      </div>
      <div className="auth-floating-card auth-floating-left" aria-hidden="true">
        <p>Lakshya IAS</p>
        <span>Daily consistency beats random intensity.</span>
      </div>
      <div className="auth-floating-card auth-floating-right" aria-hidden="true">
        <p>Exam Lens</p>
        <span>Prelims + Mains + Interview mindset</span>
      </div>
      <div className="auth-shell">
        <section className="card auth-hero">
          <div className="brand-lockup">
            <div className="brand-mark" aria-hidden="true">
              <svg viewBox="0 0 100 100" role="img" aria-label="Lakshya IAS Logo">
                <circle cx="50" cy="50" r="44" fill="none" stroke="currentColor" strokeWidth="4" />
                <circle cx="50" cy="50" r="6" fill="currentColor" />
                {Array.from({ length: 12 }).map((_, idx) => {
                  const angle = (idx * 30 * Math.PI) / 180;
                  const x1 = 50 + Math.cos(angle) * 12;
                  const y1 = 50 + Math.sin(angle) * 12;
                  const x2 = 50 + Math.cos(angle) * 38;
                  const y2 = 50 + Math.sin(angle) * 38;
                  return <line key={idx} x1={x1} y1={y1} x2={x2} y2={y2} stroke="currentColor" strokeWidth="3" />;
                })}
              </svg>
            </div>
            <div>
              <p className="brand-name">Lakshya IAS</p>
              <p className="brand-tagline">AI Mentorship Platform</p>
            </div>
          </div>
          <p className="auth-badge">Lakshya IAS AI Platform</p>
          <h1>Prepare Smarter For UPSC</h1>
          <p className="auth-hero-copy">
            Practice, evaluate, and improve with an exam focused AI mentor built for serious aspirants.
          </p>
          <div className="landmark-strip" aria-hidden="true">
            <span />
            <span />
            <span />
            <span />
            <span />
          </div>
          <div className="hero-points">
            <span>Adaptive Test Flow</span>
            <span>Mains Feedback</span>
            <span>Current Affairs</span>
          </div>
          <div className="hero-metrics">
            <div>
              <strong>24x7</strong>
              <p>AI Guidance</p>
            </div>
            <div>
              <strong>1 Dashboard</strong>
              <p>Track Progress</p>
            </div>
          </div>
        </section>

        <form className="card auth-card" onSubmit={onSubmit}>
          <div className="auth-switch" role="tablist" aria-label="Auth mode switch">
            <button
              type="button"
              className={`switch-btn ${!isSignup ? "active" : ""}`}
              onClick={() => setIsSignup(false)}
            >
              Login
            </button>
            <button
              type="button"
              className={`switch-btn ${isSignup ? "active" : ""}`}
              onClick={() => setIsSignup(true)}
            >
              Sign Up
            </button>
          </div>

          <div>
            <h2>{isSignup ? "Create Your Lakshya Account" : "Welcome Back"}</h2>
            <p className="muted auth-subtext">
              {isSignup
                ? "Build your personalized UPSC journey in under a minute."
                : "Continue your focused preparation with Lakshya AI Platform."}
            </p>
          </div>

          {error && <p className="error-text">{error}</p>}

          {isSignup && (
            <label className="form-field">
              <span>Full name</span>
              <input name="full_name" placeholder="Enter your full name" value={form.full_name} onChange={onChange} required />
            </label>
          )}

          <label className="form-field">
            <span>Email address</span>
            <input name="email" type="email" placeholder="you@example.com" value={form.email} onChange={onChange} required />
          </label>

          {isSignup && (
            <label className="form-field">
              <span>Phone number</span>
              <input name="phone" placeholder="Optional" value={form.phone} onChange={onChange} />
            </label>
          )}

          <label className="form-field">
            <span>Password</span>
            <div className="password-row">
              <input
                name="password"
                type={showPassword ? "text" : "password"}
                placeholder="Enter your password"
                value={form.password}
                onChange={onChange}
                required
              />
              <button type="button" className="ghost-btn" onClick={() => setShowPassword((v) => !v)}>
                {showPassword ? "Hide" : "Show"}
              </button>
            </div>
          </label>

          {isSignup && (
            <>
              <label className="form-field">
                <span>BPSC attempt target</span>
                <select name="bpsc_attempt" value={form.bpsc_attempt} onChange={onChange}>
                  <option value="71st">71st</option>
                  <option value="72nd">72nd</option>
                  <option value="73rd">73rd</option>
                  <option value="74th">74th</option>
                  <option value="75th+">75th+</option>
                </select>
              </label>
              <label className="check-row auth-check-row">
                <input
                  type="checkbox"
                  name="commitment_4hrs"
                  checked={form.commitment_4hrs}
                  onChange={onChange}
                />
                I commit to 4+ focused study hours today.
              </label>
            </>
          )}

          <button className="primary-btn auth-submit" type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Please wait..." : isSignup ? "Start My Journey" : "Login To Lakshya"}
          </button>

          <button className="text-btn auth-footnote" type="button" onClick={() => setIsSignup((v) => !v)}>
            {isSignup ? "Already have an account? Login" : "New user? Create an account"}
          </button>
        </form>
      </div>
    </div>
  );
}
