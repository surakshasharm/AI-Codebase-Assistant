import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  const askQuestion = async () => {
    if (!question) return;

    const userMessage = { role: "user", text: question };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/api/v1/query", {
        question: question,
      });

      const botMessage = {
        role: "bot",
        text: res.data.answer,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error(err);
      alert("Error connecting to backend");
    }

    setQuestion("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Repo Chat 🤖</h2>

      <div style={{ marginBottom: 20 }}>
        {messages.map((msg, i) => (
          <div key={i}>
            <b>{msg.role}:</b> {msg.text}
          </div>
        ))}
      </div>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about repo..."
        style={{ width: "300px", marginRight: "10px" }}
      />

      <button onClick={askQuestion}>Send</button>
    </div>
  );
}

export default App;