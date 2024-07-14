/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
  './templates/**/*.html',
  './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        lightBlue: '#A0C4FF',
        darkBlue: '#003B5C',
        lightGreen: '#C6EBC9',
        darkGreen: '#005B5D',
        white: '#FFFFFF',
        lightGray: '#F7F7F7',
        darkGray: '#4B4B4B',
      },
    },
  },
  plugins: [],
}

