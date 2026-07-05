import { NavLink, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const navItems = [
  { to: "/", label: "Home" },
  { to: "/upsc-gpt", label: "UPSC GPT" },
  { to: "/test-generator", label: "Test Generator" },
  { to: "/mains-evaluator", label: "Mains Evaluator" },
  { to: "/current-affairs", label: "Current Affairs" },
  { to: "/upsc-puzzle", label: "UPSC Puzzle" },
  { to: "/dashboard", label: "Dashboard" },
];

export default function Layout() {
  const { user, logout } = useAuth();

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1 className="brand">Lakshya</h1>
        <p className="subtitle">AI UPSC Prep Platform</p>
        <nav>
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === "/"}
              className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
        <div className="sidebar-footer">
          <p className="user-name">Hi, {user?.full_name?.split(" ")?.[0] || "Aspirant"}</p>
          <button className="secondary-btn" onClick={logout}>
            Logout
          </button>
        </div>
      </aside>
      <main className="content">
        <Outlet />
      </main>
    </div>
  );
}
