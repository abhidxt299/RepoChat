import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import CoinFlip from './CoinFlip.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <CoinFlip />
  </StrictMode>
)
