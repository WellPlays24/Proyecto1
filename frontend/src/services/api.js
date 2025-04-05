import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Cambia la URL base si es necesario
});

export default api;
