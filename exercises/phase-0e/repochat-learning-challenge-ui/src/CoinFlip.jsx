import './App.css'
import { useState } from 'react'

export default function CoinFlip() {
    {/* Build a coin flip with three UI states: idle (button only), flipping (disabled button + message), and result (outcome + running count of heads/tails)*/} 

    const [count, setCount] = useState( {heads: 0, tails: 0} )
    const [result, setResult] = useState(null)
    const [status, setStatus] = useState("idle")

    const coinFlip = () => {
        setStatus("flipping")
        setTimeout(() => {
            const outcome = Math.random() < 0.5 ? "heads" : "tails"
            setResult(outcome)
            setCount(prevCount => ({
                ...prevCount,
                [outcome]: prevCount[outcome] + 1
            }))
            setStatus("done")
        }, 1000)
    }

    return (
        <div className = 'coinFlip'>
            <button 
                onClick = { coinFlip } 
                disabled = { status === "flipping" }
            > 
            { status === "flipping" ? "Flipping..." : "Flip Coin" } 
            </button>
            { status === "flipping" && <p>🪙 The coin is in the air...</p> }
            { status === "done" && (
                <div>
                    <p> Result: {result.toUpperCase()} </p>
                    <p> Heads count: {count.heads} </p>
                    <p> Tails count: {count.tails} </p>
                </div>
                ) 
            }
        </div>
    )
}