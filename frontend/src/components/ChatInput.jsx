export default function ChatInput({

    query,
    setQuery,
    onSend

}) {

    return (

        <div className="card">

            <h2>Ask a Question</h2>

            <textarea
                rows={4}
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Summarize this PDF..."
            />

            <button
                onClick={onSend}
            >
                Send
            </button>

        </div>

    );

}