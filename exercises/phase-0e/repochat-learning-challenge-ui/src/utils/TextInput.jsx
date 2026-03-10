export function TextInput ({ text, setText }) {
    const handleKeyDown = (e) => {
        if (e.key === 'Backspace') {
            setText("")
        }
        if (e.key == 'Enter') {
            console.log("Entered text: ", text)
        }
    }
    return (
        <div>
            <input
                type = "text"
                value = {text}
                onChange = { (e) => setText(e.target.value)}
                onKeyDown = {handleKeyDown}
            />
            <p> You typed: {text} </p>
            <p> Character count of typed text: {text.length} </p>
        </div>
    )
}