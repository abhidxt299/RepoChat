import './App.css'
import { RepoCard } from './utils/RepoCard.jsx'

export default function App() {
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
    </>
  )
}