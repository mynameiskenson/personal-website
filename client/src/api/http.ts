import axios from 'axios';

const API = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api',
    timeout: 10000, // 10 seconds timeout,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default API;