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

            files.forEach((file) => {
                formData.append("files", file);
            });

            const res = await api.post(
                "/chat",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            console.log("FULL RESPONSE:");
            console.log(res.data);

            setPlan(res.data.plan);
            setContext(res.data.context);
            setResponse(res.data.response);

        } catch (err) {

            console.error("Axios Error:", err);

            if (err.response) {

                console.log("Status:", err.response.status);
                console.log("Backend Response:", err.response.data);

                alert(
                    JSON.stringify(err.response.data, null, 2)
                );

            } else {

                console.log("Message:", err.message);

                alert(err.message);

            }

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