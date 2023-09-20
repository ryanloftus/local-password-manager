const React = require('react');
const { createRoot } = require('react-dom/client');
const { App } = require('./components/App.jsx');

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
