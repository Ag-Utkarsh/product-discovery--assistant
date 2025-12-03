/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Helvetica', 'Arial', 'sans-serif'],
            },
            colors: {
                primary: '#000000',
                secondary: '#fafafa',
            }
        },
    },
    plugins: [],
}
