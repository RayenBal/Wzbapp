from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel
import os

# ✅ Declare FastAPI app first
app = FastAPI()

# ✅ Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Centralized model name to filename mapping
model_file_map = {
    "xgboost": "XGBoost",
    "randomforest": "RF",
    "bilstm": "BiLSTM",
    "transformer": "Transformer"
}

# ✅ Generic file path resolver
def get_file_path(model: str, filetype: str):
    model_folder = f"app/data/{model}"
    filename = f"{filetype}_{model_file_map[model]}.csv"
    return os.path.join(model_folder, filename)

# ✅ Metrics endpoint
@app.get("/metrics/{model}")
def get_metrics(model: str):
    filepath = get_file_path(model, "evaluation_metrics")
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")

# ✅ Feature importance endpoint
@app.get("/feature-importance/{model}")
def get_feature_importance(model: str):
    filepath = get_file_path(model, "feature_importance")
    df = pd.read_csv(filepath, index_col=0)
    return df.to_dict()

# ✅ Residuals endpoint
@app.get("/residuals/{model}")
def get_residuals(model: str):
    filepath = get_file_path(model, "residuals")
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")

@app.get("/predictions/{model}")
def get_predictions(model: str):
    model_file_map = {
        "xgboost": "XGBoost",
        "randomforest": "RF",
        "bilstm": "BiLSTM",
        "transformer": "Transformer"
    }
    model_file = model_file_map.get(model)
    filepath = f"app/data/{model}/PastFuture_Predictions_{model_file}.csv"
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")
