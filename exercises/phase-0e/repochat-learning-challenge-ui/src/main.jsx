import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import CoinFlip from './CoinFlip.jsx'
import ListAndKeys from './ListAndKeys.jsx'
import FetchRepo from './FetchRepo.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <CoinFlip />
    <ListAndKeys />
    <FetchRepo />
  </StrictMode>
)
