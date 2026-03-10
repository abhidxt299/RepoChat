import './App.css'
import { RepoCard } from './utils/RepoCard.jsx'
import { useState } from 'react'

export default function App() {
  
  const [count, setCount] = useState(0)

  return (
    <>
      <div className = "profile">
        <h1>Abhishek Dixit</h1>
        <h3>SDE to ML Engineer</h3>
        <p>Building RepoChat to learn RAG and vector databases.</p>
      </div>
      <div className = "repo-cards">
        <RepoCard name="fastapi" stars={75000} />
        <RepoCard name="react"   stars={220000} />
        <RepoCard name="flask"   stars={66000} />
      </div>
      <div>
        <h2> Count: {count} </h2>
        <button onClick = { () => setCount(count + 1) }> Clicking increases count by 1 </button>
        <button onClick = { () => setCount(count - 1) }> Clicking decreases count by 1 </button>
        <button onClick = { () => setCount(0) }> Clicking resets the count </button>
      </div>
    </>
  )
}