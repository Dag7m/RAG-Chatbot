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

    const currentQuery = query; // Capture scope before state clear
    const userMessage = { type: "user", text: currentQuery };
    setMessages((prev) => [...prev, userMessage]);

    setQuery(""); // ⚡ Instantly clear input field
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        query: currentQuery,
      });

      const botMessage = {
        type: "bot",
        text: res.data.response,
        sources: res.data.sources,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };
  useEffect(() => {
    const loadHistory = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/history");

        const formatted = [];

        res.data.history.forEach((item) => {
          formatted.push({ type: "user", text: item.user });
          formatted.push({ 
            type: "bot", 
            text: item.assistant, 
            sources: item.sources || [] 
          });
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
    // Hide filename pill after 4 secs to keep interface clean
    setTimeout(() => setFileName(""), 4000);

    const userMsg = {
      type: "user",
      text: `I uploaded a file: ${file.name}`,
    };
    setMessages((prev) => [...prev, userMsg]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await axios.post("http://127.0.0.1:8000/upload", formData);

      const botMsg = {
        type: "bot",
        // ✅ Uses dynamic message from the backend which explicitly names the file
        text: res.data.message || `File '${file.name}' processed and added to the knowledge base.`,
      };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: `Failed to upload file '${file.name}'.` }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>Da Chatbot</h1>
      </header>
      <div className="chat-container">
        {loading && (
          <div className="thinking-dots">
            <span></span>
            <span></span>
            <span></span>
          </div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.type}`}>
            <div>{msg.text}</div>

            {/* ✅ SHOW SOURCES ONLY FOR BOT */}
            {msg.type === "bot" && msg.sources && msg.sources.length > 0 && (
              <div className="sources">
                <b>Sources (Top 2 Closest Matches):</b>
                {msg.sources.map((src, idx) => (
                  <p key={idx}>{src}</p>
                ))}
              </div>
            )}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="input-container">
        <label className="upload-btn">
          {fileName && <span className="file-name-pill">{fileName}</span>}
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
            <polyline points="17 8 12 3 7 8"></polyline>
            <line x1="12" y1="3" x2="12" y2="15"></line>
          </svg>
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
