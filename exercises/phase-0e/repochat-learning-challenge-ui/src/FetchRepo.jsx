import { useState, useEffect } from "react";

export default function FetchRepo () {
    
    const [repo, setRepo] = useState("tiangolo/fastapi");
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`https://api.github.com/repos/${repo}`)
            .then(response => response.json())
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(error => console.error("Error fetching repository: ", error));
    }, [repo]);

    if (loading) {
        return <p>Loading...</p>;
    }
    return (
        <div>
            <h2> Enter a GitHub repository: </h2>
            <input defaultValue = {repo} onKeyDown = {e => e.key === "Enter" && setRepo(e.target.value)} />
            <p> Repository: {data.full_name} </p>
            <p> Description: {data.description} </p>
            <p> Stars: {data.stargazers_count} </p>
            <p> Forks: {data.forks_count} </p>
        </div>
    )
}