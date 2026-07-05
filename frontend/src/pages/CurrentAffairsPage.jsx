import { useState } from "react";
import { apiRequest } from "../api/client";

export default function CurrentAffairsPage() {
  const [date, setDate] = useState("");
  const [category, setCategory] = useState("");
  const [items, setItems] = useState([]);

  const fetchItems = async () => {
    const params = new URLSearchParams();
    if (date) params.set("selected_date", date);
    if (category) params.set("category", category);
    const data = await apiRequest(`/current-affairs?${params.toString()}`);
    setItems(data.items || []);
  };

  return (
    <div className="grid gap-16">
      <div className="card">
        <h2>Current Affairs</h2>
        <div className="grid two-col">
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
          <input value={category} onChange={(e) => setCategory(e.target.value)} placeholder="Tag/category" />
        </div>
        <button className="primary-btn" onClick={fetchItems}>
          Apply Filter
        </button>
      </div>

      <div className="grid gap-12">
        {items.map((item) => (
          <article key={item.id} className="card">
            <h3>{item.title}</h3>
            <p>{item.description}</p>
            <p className="muted">
              {item.tags.join(" | ")} | {item.published_on}
            </p>
          </article>
        ))}
      </div>
    </div>
  );
}
