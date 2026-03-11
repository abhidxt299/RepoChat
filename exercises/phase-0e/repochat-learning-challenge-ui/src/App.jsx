import './App.css'
import { RepoCard } from './utils/RepoCard.jsx'
import { useState } from 'react'
import { Count } from './utils/Count.jsx'
import { TextInput } from './utils/TextInput.jsx'

export default function App() {
  
  const [text, setText] = useState("")
  const [count, setCount] = useState(0)

  return (
    <>
    {/*First Challenge = Create a profile section with your name, title, and a short bio.*/}
      <div className = "profile">
        <h1>Abhishek Dixit</h1>
        <h3>SDE to ML Engineer</h3>
        <p>Building RepoChat to learn RAG and vector databases.</p>
      </div>
    {/*Second Challenge = Create a section that displays a list using a component.*/}
      <div className = "repo-cards">
        <RepoCard name="fastapi" stars={75000} />
        <RepoCard name="react"   stars={220000} />
        <RepoCard name="flask"   stars={66000} />
      </div>
    {/*Third Challenge = Create a section with an input field and a button that updates the state.*/}
      <div className = "count">
        <Count count = {count} setCount = {setCount} />
      </div>
    {/*Fourth Challenge = Create a section with an input field and a button that updates the state.*/}
      <div className = "text-input">
        <TextInput text = {text} setText = {setText} />
      </div>
    </>
  )
}