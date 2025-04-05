import React, { useState } from 'react';
import Login from './components/Login';

function App() {
  const [token, setToken] = useState(null);

  return (
    <div className="App">
      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <h2>Bienvenido, usuario autenticado</h2>  // Aquí puedes agregar más funcionalidades cuando el usuario esté logueado
      )}
    </div>
  );
}

export default App;
