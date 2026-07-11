export default function ChatWindow({ response }) {

    return (

        <div className="card">

            <h2>Final Response</h2>

            <div
                style={{
                    whiteSpace: "pre-wrap",
                    lineHeight: "1.7",
                    fontSize: "15px"
                }}
            >
                {response || "Waiting for AI response..."}
            </div>

        </div>

    );

}