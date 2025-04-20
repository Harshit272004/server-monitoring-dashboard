# Server Monitoring Dashboard (Full Stack App)

A web-based **Server Monitoring Dashboard** built using **FastAPI (Python)** for the backend, **ReactJS (Vite)** for the frontend, and **PostgreSQL** for the database.

The app allows users to authenticate and view real-time system metrics, network traffic, and audit logs across multiple servers.

---

## 🔗 Hosted Links

- **Frontend (React + Netlify):** [peppy-kheer-3778b4.netlify.app](https://peppy-kheer-3778b4.netlify.app)
- **Backend (FastAPI + Render):** [https://monitoring-backend-siuy.onrender.com](https://monitoring-backend-siuy.onrender.com)
---

## ✅ Features

- JWT-based login system  
- Role-based access control (Admin, Viewer)  
- Real-time system metrics:
  - CPU, RAM, Disk, and Application Usage (charts)
  - Network traffic graph  
- Alert count indicators: Critical, Medium, Low  
- Server info listing  
- Audit logging middleware  

---

## ⚙️ Tech Stack

| Layer     | Technology                          |
|-----------|--------------------------------------|
| Frontend  | ReactJS (Vite), Axios, Recharts      |
| Backend   | FastAPI, Pydantic, SQLAlchemy        |
| Database  | PostgreSQL (Railway)                 |
| Hosting   | Netlify (Frontend), Render (Backend) |

---

## 📁 Folder Structure

```
server-monitoring-dashboard/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── audit.py
│   │   └── routes/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── public/
│   │   └── _redirects
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── package.json
│   └── vite.config.js
```

---

## ⚡ Setup Instructions

### ▶️ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Initialize the database:

```bash
python app/create_tables.py
python app/mock_data.py
```

Run the server locally:

```bash
uvicorn app.main:app --reload
```

---

### ▶️ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🚀 Deployment Details

### Netlify (Frontend)

- **Build command:** `npm run build`
- **Publish directory:** `dist`
- **Base directory:** `frontend`
- `_redirects` file in `frontend/public/`:

```
/*    /index.html   200
```

### Render (Backend)

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- **Root directory:** `backend/`
- Tables are automatically created using SQLAlchemy on app start.

---

## 💬 Interview Talking Points

- Full-stack architecture using FastAPI and React  
- Role-based authentication using JWT  
- FastAPI middleware for API request auditing  
- SPA routing fixed on Netlify using `_redirects`  
- Real-time metric updates using mocked data (extensible)  
- PostgreSQL hosted securely via Railway  
- CI/CD with environment variables via Netlify & Render  

---

## 👨‍💻 Author

**Harshit Vyas**  
GitHub: [@Harshit272004](https://github.com/Harshit272004)

---

## 📄 License

**MIT License**
