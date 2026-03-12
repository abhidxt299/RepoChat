import './App.css'
import { useState } from 'react'

export default function ListAndKeys() {
    {/* Build a list of items from an array of data, ensuring each item has a unique key.*/}

    const [todos, setTodos] = useState([
        { id: 1, text: "Learn React" },
        { id: 2, text: "Build a todo app" },
        { id: 3, text: "Deploy the app" }
    ])

    const [input, setInput] = useState("")

    const addTodo = () => {
        if (input.trim() === "") return
        const newTodo = { id: Date.now(), text: input }
        setTodos(prevTodos => [...prevTodos, newTodo])
        setInput("")
    }

    const removeTodo = (id) => {
        if (todos.length === 0) return
        setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id))
    }

    return (
        <div className = "list-and-keys">
            <h2>To-Do List: </h2>
            <input
                type = "text"
                value = { input }
                onChange = {e => setInput(e.target.value)}
                placeholder = "Add a new task"
            />
            <button onClick = {addTodo}>Add Task</button>
            <ul>
                { todos.map(todo => (
                    <li key = {todo.id}>{todo.text} 
                        <button onClick = {() => removeTodo(todo.id)}>
                        Remove
                        </button>
                    </li>
                )) }
            </ul>
        </div>
    )
}