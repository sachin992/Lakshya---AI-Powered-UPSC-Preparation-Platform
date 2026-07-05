import { useMemo, useState } from "react";
import { apiRequest } from "../api/client";

export default function UpscGptPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [threadId] = useState(() => crypto.randomUUID());
  const [uploadNote, setUploadNote] = useState("");
  const [chatDarkMode, setChatDarkMode] = useState(true);

  const canSend = useMemo(() => input.trim().length > 0 && !loading, [input, loading]);

  const send = async () => {
    if (!canSend) return;
    const userMsg = input.trim();
    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: userMsg }]);
    setLoading(true);
    try {
      const data = await apiRequest("/upsc-gpt/chat", {
        method: "POST",
        body: JSON.stringify({ message: userMsg, thread_id: threadId }),
      });
      setMessages((prev) => [...prev, { role: "assistant", content: data.response }]);
    } catch (err) {
      setMessages((prev) => [...prev, { role: "assistant", content: `Error: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  const uploadPdf = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      const data = await apiRequest(`/upsc-gpt/upload?thread_id=${encodeURIComponent(threadId)}`, {
        method: "POST",
        body: formData,
      });
      setUploadNote(`Indexed: ${data.metadata.filename} (${data.metadata.chunks} chunks)`);
    } catch (err) {
      setUploadNote(`Upload failed: ${err.message}`);
    }
  };

  return (
    <div className="grid gap-16">
      <div className="card">
        <h2>UPSC GPT</h2>
        <p className="muted">Thread ID: {threadId}</p>
        <input type="file" accept="application/pdf" onChange={uploadPdf} />
        {uploadNote && <p className="muted">{uploadNote}</p>}
      </div>

      <div className={`card chat-box ${chatDarkMode ? "chat-box-dark" : ""}`}>
        <div className="chat-toolbar">
          <p className="muted">Lakshya chat mode</p>
          <button className="secondary-btn" type="button" onClick={() => setChatDarkMode((v) => !v)}>
            {chatDarkMode ? "Dark On" : "Dark Off"}
          </button>
        </div>
        <div className="chat-messages">
          {messages.map((m, i) => (
            <div key={i} className={`msg ${m.role} ${chatDarkMode ? "dark" : ""}`}>
              <strong>{m.role === "user" ? "You" : "Lakshya"}:</strong> {m.content}
            </div>
          ))}
          {loading && <p className={`muted ${chatDarkMode ? "chat-loading-dark" : ""}`}>Thinking...</p>}
        </div>
        <div className="chat-input-row">
          <input
            className={chatDarkMode ? "chat-input-dark" : ""}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask UPSC question..."
          />
          <button className="primary-btn" onClick={send} disabled={!canSend}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
