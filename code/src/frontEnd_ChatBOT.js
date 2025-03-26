import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
const [query, setQuery] = useState("");
const [response, setResponse] = useState("");

const sendQuery = async () => {
try {
const res = await axios.post("http://localhost:8000/chat/", { user_query: query });
setResponse(res.data.response);
} catch (error) {
console.error("Error:", error);
setResponse("Error fetching response.");
}
};

return (
<div>
<h2>AI Chatbot</h2>
<input
type="text"
value={query}
onChange={(e) => setQuery(e.target.value)}
placeholder="Ask something..."
/>
<button onClick={sendQuery}>Send</button>
<p><strong>Response:</strong> {response}</p>
</div>
);
};

export default Chatbot;