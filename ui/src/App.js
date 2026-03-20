import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [fileName, setFileName] = useState("");
  const chatEndRef = useRef(null);

useEffect(() => {
  chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
}, [messages]);

  const sendMessage = async () => {
  if (!query.trim()) return;

  const userMessage = { type: "user", text: query };
  setMessages((prev) => [...prev, userMessage]);

  setLoading(true);

  try {
    const res = await axios({
      method: "post",
      url: "http://127.0.0.1:8000/chat",
      headers: {
        "Content-Type": "application/json",
      },
      data: {
        query: query,
      },
    });

    const botMessage = { type: "bot", text: res.data.response };

    setMessages((prev) => [...prev, botMessage]);
  } catch (err) {
    console.error("Chat error:", err.response?.data || err.message);
    alert("Chat failed. Check backend.");
  }

  setLoading(false);
  setQuery("");
};

  useEffect(() => {
  const loadHistory = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/history");

      const formatted = [];

      res.data.history.forEach((item) => {
        formatted.push({ type: "user", text: item.user });
        formatted.push({ type: "bot", text: item.assistant });
      });

      setMessages(formatted);
    } catch (err) {
      console.error("Failed to load history", err);
    }
  };

  loadHistory();
}, []);

  const handleUpload = async (e) => {
  const file = e.target.files[0];

  if (!file) return;

  setFileName(file.name);

  const formData = new FormData();
  formData.append("file", file);

  await axios.post("http://127.0.0.1:8000/upload", formData);

  alert("File uploaded!");
};

  return (
    <div className="app">
      <div className="chat-container">
        {loading && <div className="message-bot">Thinking...</div>}
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.type}`}>
            {msg.text}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="input-container">
        <label className="upload-btn">
        {fileName && <span className="file-name">{fileName}</span>}
  +
  <input type="file" onChange={handleUpload} hidden />
</label>

        <input
          className="input-box"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;