export function Count({ count, setCount }) {
    return (
        <div>
            <h2> Count: {count} </h2>
            <button onClick = { () => setCount(count + 1) }> Clicking increases count by 1 </button>
            <button onClick = { () => setCount(count - 1) }> Clicking decreases count by 1 </button>
            <button onClick = { () => setCount(0) }> Clicking resets the count </button>
        </div>
    )
}