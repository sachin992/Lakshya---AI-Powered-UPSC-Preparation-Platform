import { Navigate, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import ProtectedRoute from "./components/ProtectedRoute";
import CurrentAffairsPage from "./pages/CurrentAffairsPage";
import DashboardPage from "./pages/DashboardPage";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import MainsEvaluatorPage from "./pages/MainsEvaluatorPage";
import PuzzlePage from "./pages/PuzzlePage";
import TestGeneratorPage from "./pages/TestGeneratorPage";
import UpscGptPage from "./pages/UpscGptPage";

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Layout />
          </ProtectedRoute>
        }
      >
        <Route index element={<HomePage />} />
        <Route path="upsc-gpt" element={<UpscGptPage />} />
        <Route path="test-generator" element={<TestGeneratorPage />} />
        <Route path="mains-evaluator" element={<MainsEvaluatorPage />} />
        <Route path="current-affairs" element={<CurrentAffairsPage />} />
        <Route path="upsc-puzzle" element={<PuzzlePage />} />
        <Route path="dashboard" element={<DashboardPage />} />
      </Route>
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
