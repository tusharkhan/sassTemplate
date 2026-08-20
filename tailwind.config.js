/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');
const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./*.html', './documentation/**/*.html', './assets/js/**/*.js'],
  darkMode: 'class',
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1.25rem',
        sm: '1.5rem',
        lg: '2rem',
      },
    },
    extend: {
      colors: {
        // Primary brand color — change these two lines to re-skin the template
        primary: colors.indigo,
        accent: colors.cyan,
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', ...defaultTheme.fontFamily.sans],
        mono: ['"JetBrains Mono"', ...defaultTheme.fontFamily.mono],
      },
      boxShadow: {
        'glow-sm': '0 0 20px -4px rgb(99 102 241 / 0.45)',
        glow: '0 0 40px -8px rgb(99 102 241 / 0.5)',
        'glow-lg': '0 0 80px -12px rgb(99 102 241 / 0.55)',
        'glow-accent': '0 0 40px -8px rgb(6 182 212 / 0.45)',
      },
      animation: {
        float: 'float 6s ease-in-out infinite',
        'float-slow': 'float 9s ease-in-out infinite',
        'pulse-soft': 'pulse-soft 3s ease-in-out infinite',
        'equalizer-1': 'equalizer 1.1s ease-in-out infinite',
        'equalizer-2': 'equalizer 1.4s ease-in-out infinite 0.2s',
        'equalizer-3': 'equalizer 0.9s ease-in-out infinite 0.1s',
        'equalizer-4': 'equalizer 1.3s ease-in-out infinite 0.3s',
        'equalizer-5': 'equalizer 1s ease-in-out infinite 0.15s',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        'pulse-soft': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.55' },
        },
        equalizer: {
          '0%, 100%': { transform: 'scaleY(0.35)' },
          '50%': { transform: 'scaleY(1)' },
        },
      },
    },
  },
  plugins: [],
};
