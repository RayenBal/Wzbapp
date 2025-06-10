# Wzbapp

This repository contains a small FastAPI backend and a simple frontend used to visualize model metrics.

## Running the backend

Create and activate a Python environment, install dependencies and run the API:

```bash
uvicorn backend.app.main:app --reload
```

## Viewing the frontend

Open `frontend/index.html` in your browser. It allows selecting a model and fetching metrics, feature importance, residuals and predictions dynamically from the backend.
