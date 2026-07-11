export default function PlanTrace({ plan }) {

    return (

        <div className="card">

            <h2>Execution Plan</h2>

            {!plan ? (

                <p>No execution yet.</p>

            ) : (

                <div>

                    <p><strong>Intent:</strong> {plan.intent}</p>

                    <p><strong>Tools:</strong></p>

                    <ul>

                        {plan.tools.map((tool, index) => (

                            <li key={index}>
                                {tool}
                            </li>

                        ))}

                    </ul>

                </div>

            )}

        </div>

    );

}