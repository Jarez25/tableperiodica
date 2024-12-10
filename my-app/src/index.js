import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

// Renderiza el componente App en el div con id 'root' en tu HTML
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
