# Wzbapp

This repository contains a small FastAPI backend and a simple frontend used to visualize model metrics.

## Running the backend

Create and activate a Python environment, install dependencies and run the API:

```bash
uvicorn backend.app.main:app --reload
```

## Viewing the frontend

Open `frontend/index.html` in your browser. The page uses Bootstrap and Chart.js to render metrics tables and interactive charts for feature importance, residuals and predictions.
Select a model from the dropdown and press **Load Data** to visualise the results.
