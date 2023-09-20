/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/index.html',
    './src/components/*.jsx',
  ],
  plugins: [require('daisyui')],
}

