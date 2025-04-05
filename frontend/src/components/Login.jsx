import React, { useState } from 'react';
import api from '../services/api';  // Importamos la configuración de Axios

const Login = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('login/', {
        username,
        password,
      });

      // Guardamos el token en el estado (puedes guardarlo también en el localStorage)
      setToken(response.data.access_token);
      setError(null);  // Limpiamos el error si el login fue exitoso
    } catch (err) {
      // Si hay un error, mostramos el mensaje
      setError('Credenciales incorrectas');
    }
  };

  return (
    <div className="login-form">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
