# backend/app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pickle
from pydantic import BaseModel

# تحميل الموديل مرة واحدة
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI(title="House Price Prediction API")

# سماح للـ frontend بالوصول أثناء التطوير
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # في الإنتاج غيّرها للدومين بتاعك فقط
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HouseData(BaseModel):
    size_sqft: int
    bedrooms: float

@app.get("/")
async def home():
    return {"message":"Welcome to the House Price Prediction API"}

@app.post("/predict")
async def predict(data: HouseData):
    try:
        features = np.array([[data.size_sqft, data.bedrooms]])
        prediction = model.predict(features)
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
