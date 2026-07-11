export default function ExtractedText({ context }) {

    return (

        <div className="card">

            <h2>Extracted Text</h2>

            <pre>

                {context || "No extracted content."}

            </pre>

        </div>

    );

}