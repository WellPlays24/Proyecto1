# My App

Proyecto fullstack con Django (backend) y Vite + React (frontend).

## Estructura

my-app/ 
├── backend/ ← Backend con Django 
├── frontend/ ← Frontend con Vite + React 
├── .gitignore 
├── README.md 
└── docker-compose.yml (opcional)


## Requisitos

- Python 3.8+
- Node.js y npm

## Instalación

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
python manage.py runserver

### Backend

cd frontend
npm install
npm run dev


---

### ⚙️ `docker-compose.yml` (opcional)

Si planeas usar Docker más adelante, este archivo te puede servir para levantar ambos servicios juntos. Te puedo ayudar a generarlo cuando lo necesites.

---

¿Quieres que subamos ya todo a GitHub o necesitas algo más antes de hacer el primer commit?

