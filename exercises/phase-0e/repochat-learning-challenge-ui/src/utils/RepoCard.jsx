export function RepoCard({ name, stars }) {
  return (
    <div>
      <h3>{name}</h3>
      <p>{stars.toLocaleString()} stars</p>
    </div>
  )
}