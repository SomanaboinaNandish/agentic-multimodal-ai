import { useState } from "react";
import api from "../services/api";

import Navbar from "../components/Navbar";
import FileUploader from "../components/FileUploader";
import ChatInput from "../components/ChatInput";
import ChatWindow from "../components/ChatWindow";
import PlanTrace from "../components/PlanTrace";
import ExtractedText from "../components/ExtractedText";

import "../styles/home.css";

export default function Home() {

    const [files, setFiles] = useState([]);
    const [query, setQuery] = useState("");

    const [plan, setPlan] = useState(null);
    const [context, setContext] = useState("");
    const [response, setResponse] = useState("");

    async function sendMessage() {

        try {

            const formData = new FormData();

            formData.append("query", query);

            files.forEach(file => {
                formData.append("files", file);
            });

            const res = await api.post("/chat", formData);

setPlan(res.data.plan);
setContext(res.data.context);
console.log("Response from backend:", res.data.response);

alert(res.data.response);

setResponse(res.data.response);

        } catch (err) {

            console.error(err);

            alert("Backend request failed");

        }

    }

    return (

        <div className="container">

            <Navbar />

            <FileUploader
                files={files}
                setFiles={setFiles}
            />

            <ChatInput
                query={query}
                setQuery={setQuery}
                onSend={sendMessage}
            />

            <PlanTrace plan={plan} />

            <ExtractedText context={context} />

            <ChatWindow response={response} />

        </div>

    );

}