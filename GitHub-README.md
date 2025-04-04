# Guía para colaboradores

Bienvenido al proyecto 🎉  
Esta guía te ayudará a clonar el repositorio, levantar el proyecto localmente y contribuir de forma ordenada usando Git.

---

## 🔧 Requisitos previos

- Python 3.8+
- Node.js y npm
- Git

---

## 🧪 Paso 1: Clonar el repositorio

```bash
git clone https://github.com/WellPlays24/Proyecto1.git
cd Proyecto1


📦 Paso 2: Preparar el backend (Django)

cd backend
python -m venv venv
# Activar el entorno virtual:
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

# Ejecutar el servidor
python manage.py runserver


💻 Paso 3: Preparar el frontend (Vite + React)

cd ../frontend
npm install
npm run dev

🌱 Paso 4: Trabajar desde una rama
Nunca trabajes directamente en master. Usa ramas para cada módulo o tarea.

# Asegúrate de estar en la raíz del proyecto
git checkout -b feature/nombre-de-tu-rama

Ejemplo:
git checkout -b feature/login-form

✅ Paso 5: Hacer commits
git add .
git commit -m "Descripción clara de lo que hiciste"

⬆️ Paso 6: Subir tu rama
git push -u origin feature/nombre-de-tu-rama

🔁 Paso 7: Crear un Pull Request
Ve a GitHub: https://github.com/WellPlays24/Proyecto1

Verás un botón para "Compare & Pull Request"
Describe los cambios realizados y crea el PR hacia master

📌 Reglas de colaboración
Trabaja siempre desde tu propia rama
Haz commits frecuentes y con mensajes claros
Usa Pull Requests para unir tu trabajo a master
Revisa y comenta los PRs de otros si puedes







